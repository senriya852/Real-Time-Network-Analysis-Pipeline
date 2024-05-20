# Real-Time Network Analysis Pipeline
![image](https://github.com/senriya852/Real-Time-Network-Analysis-Pipeline/blob/main/image/pipeline_architecture.png)

## Steps

1. **Generate Packets**
   - Use Python code to generate network packets.

2. **Remove GTP Layer**
   - If the GTP layer is present in packets, use the TraceWrangler tool to remove it. Otherwise, skip this step.

3. **Convert pcapng to pcap**
   - Use the Tshark tool to convert the file from `pcapng` to `pcap`.

4. **Convert pcap to Network Flows in CSV Format**
   - Use the Argus tool to convert the file from `pcap` to network flows and then to CSV format.

5. **Encode CSV File**
   - Use Python code to encode the CSV file.

6. **Extract Required Features**
   - Use Python code to extract the necessary features from the encoded CSV file.

7. **Train the Encoded CSV File on Machine Learning Model**
   - Use the encoded CSV file to train a machine learning model.


