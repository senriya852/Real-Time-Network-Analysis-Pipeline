python3 packet.py 
tshark -F pcap -r captured_packets.pcapng -w captured_packets.pcap  
argus -r captured_packets.pcap -w captured_packets.argus   
ra -r  captured_packets.argus -u -s  proto > proto.csv 
ra -r  captured_packets.argus -u -s  sttl > sttl.csv
ra -r  captured_packets.argus -u -s  offset > offset.csv
ra -r  captured_packets.argus -u -s  state > state.csv
ra -r  captured_packets.argus -u -s  seq > seq.csv
ra -r  captured_packets.argus -u -s  smeansz > smeansz.csv
ra -r  captured_packets.argus -u -s  ackdat > ackdat.csv
ra -r  captured_packets.argus -u -s  tcprtt > tcprtt.csv
python3 csv_merge.py 
python3 process_final.py 
python3 Random_forest.py 