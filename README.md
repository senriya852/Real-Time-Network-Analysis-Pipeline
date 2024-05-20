# Real-Time Network Analysis Pipeline
![image](https://github.com/senriya852/Real-Time-Network-Analysis-Pipeline/blob/main/image/pipeline_architecture.png)


Step 1: **Generate Packets**
   - Use Python code to generate network packets.
   - Run file packet.py
![image](https://github.com/senriya852/Real-Time-Network-Analysis-Pipeline/blob/main/image/generated_packets.png)


Step 2: **Remove GTP Layer**
   - If the GTP layer is present in packets, use the TraceWrangler tool to remove it. If not, you can skip this step.

Step 3: **Convert packets in pcapng to pcap format**
   - Use the Tshark tool to convert the file from `pcapng` to `pcap`.

Step 4: **Convert pcap file to Network Flows then in CSV Format**
   - Use the Argus tool to convert the file from `pcap` to network flows and then to CSV format.

Step 5: **Encode CSV File**
   - Use Python code to encode the CSV file.

Step 6: **Extract Required Features**
   - Use Python code to extract the necessary features from the encoded CSV file.

Step 7: **Train the Encoded CSV File on Machine Learning Model**
   - Use the encoded CSV file to train a machine-learning model.
   - We use Random forest here that is "Random_forest.sav"
   - ![image](https://github.com/senriya852/Real-Time-Network-Analysis-Pipeline/blob/main/image/results.png)


