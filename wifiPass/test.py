
import sys
import socket
import struct
 
filename = sys.argv[0]
filename = sys.argv[1]
#print filename
ipaddr = sys.argv[2]
direction = sys.argv[3]
 
packed = socket.inet_aton(ipaddr)
ip32 = struct.unpack("!L", packed)[0]
 
file = open(filename, "rb") 
 
pkthdrlen=16
iphdrlen=20
tcphdrlen=20
stdtcp = 20
total = 0
pos = 0
 
start_seq = 0
end_seq = 0
 
# Read file header(type and size)
typedata = file.read(8)
(type, size) = struct.unpack("=LL", typedata)
 
# Skip header description
skipdata = file.read(size-8)
 
# Read interface desc block
interfacedata = file.read(8)
(type, size) = struct.unpack("=LL", interfacedata)
 
# Get linktype from int-desc block
ltdata = file.read(4)
(type, ltsize) = struct.unpack("=HH", ltdata)
if ltsize == 0x71:
	pkthdrlen = 16
else:
	pkthdrlen = 14
 
# Skip other of int-desc block
skipdata = file.read(size-8-4)
 
# Read packet block
pktdata = file.read(8)
(type, size) = struct.unpack("=LL", pktdata)
 
ipcmp = 0
cnt = 0
 
while pktdata:
	# Skip Interface ID
	skipdata = file.read(4)
 
	# Get time and length
	# sec:
	# microsec:
	# iplensave:
	# origlen:
	data = file.read(16)
	(sec, microsec, iplensave, origlen) = struct.unpack("=LLLL", data)
 
	# Read linklayer
	linkdata = file.read(pkthdrlen)
	
 
	# Read IP header
	ipdata = file.read(iphdrlen)
	(vl, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr) = struct.unpack(">ssHHHssHLL", ipdata)
	iphdrlen = ord(vl) & 0x0F 
	iphdrlen *= 4
 
	# Read TCP standard header
	tcpdata = file.read(stdtcp)	
	(sport, dport, seq, ack_seq, pad1, win, check, urgp) = struct.unpack(">HHLLHHHH", tcpdata)
	tcphdrlen = pad1 & 0xF000
	tcphdrlen = tcphdrlen >> 12
	tcphdrlen = tcphdrlen*4
	
	if direction == 'out':
		ipcmp = saddr
	else:
		ipcmp = daddr
 
	if ipcmp == ip32:
		cnt += 1
		total += tot_len
		total -= iphdrlen + tcphdrlen
		if start_seq == 0:  # BUG?
			start_seq = seq
		end_seq = seq
 
	# Skip options and data
	skipdata = file.read(size - 8 - 4 - 16 - pkthdrlen - iphdrlen - stdtcp)
	
	# Read next packet
	pos += 1
	pktdata = file.read(8)
	(type, size) = struct.unpack("=LL", pktdata)
	if type <> 0x06:
		break
# Get interface statistics
if type == 0x05:
	skiphdr = file.read(12)
	opthdr = file.read(4)
	(code, length) = struct.unpack("=HH", opthdr)
 
	while length <> 0:
		# 32-bit boundary! BUG?
 
		if code == 5:
			opt = file.read(length)
			(drops,) = struct.unpack("=Q", opt)
			# 不能这么将丢弃的数据包算进去！抓包时就这一个流吗？每个被丢弃的包都是携带数据的吗？...
			# 所以，pcapng仅仅统计被丢弃的数据包的数量，不够！怎么才够？不知道！！
#			total += drops*1460
	
		elif code == 7:
			opt = file.read(length)
			(drops,) = struct.unpack("=Q", opt)
#			total += drops*1460
 
		else:
			skipopt = file.read(length)
		opthdr = file.read(4)
		(code, length) = struct.unpack("=HH", opthdr)
		
 
print pos, 'Actual:'+str(total),  'ideal:'+str(end_seq-start_seq)