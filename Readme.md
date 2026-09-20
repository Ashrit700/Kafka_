3. Kafka Topics
Create a topic
.\bin\windows\kafka-topics.bat --create --topic system-metrics --bootstrap-server localhost:9092

Create with partitions:

.\bin\windows\kafka-topics.bat --create --topic system-metrics --partitions 3 --bootstrap-server localhost:9092

Create with partitions and replication factor:

.\bin\windows\kafka-topics.bat --create --topic system-metrics --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092

For a single local broker, replication factor must normally be 1.

4. List Topics

Show all topics:

.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092

Example:

system-metrics
application-logs
network-metrics
5. Describe a Topic
.\bin\windows\kafka-topics.bat --describe --topic system-metrics --bootstrap-server localhost:9092

This gives information about:

Topic
Partition
Leader
Replicas
ISR
6. Delete a Topic
.\bin\windows\kafka-topics.bat --delete --topic system-metrics --bootstrap-server localhost:9092

Verify:

.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092