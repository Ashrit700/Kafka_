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

















# Apache Kafka on GitHub Codespaces

This guide sets up **Apache Kafka 4.0.0 directly inside GitHub Codespaces** using the Linux environment.

> This setup does **not** use Docker.
>
> The commands are intentionally kept close to the Windows Kafka workflow so that commands already learned on Windows/WSL can be transferred easily to Codespaces.

---

## 1. Architecture

```text
GitHub Codespace
│
├── Java 17
│
└── Kafka 4.0.0
    │
    ├── Kafka Broker
    │
    ├── Topic: ashrit
    │
    ├── Producer
    │
    └── Consumer
```

---

# 2. Requirements

The Codespace should have:

* GitHub Codespaces
* Linux terminal
* Java 17+
* Internet connection

Check Java:

```bash
java -version
```

If Java is not installed:

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
```

Verify:

```bash
java -version
```

---

# 3. Download Apache Kafka

Go to the home directory:

```bash
cd ~
```

Download Kafka:

```bash
wget https://downloads.apache.org/kafka/4.0.0/kafka_2.13-4.0.0.tgz
```

Extract it:

```bash
tar -xzf kafka_2.13-4.0.0.tgz
```

Rename the extracted folder:

```bash
mv kafka_2.13-4.0.0 kafka
```

Enter Kafka:

```bash
cd ~/kafka
```

Check the installation:

```bash
ls
```

You should see directories/files similar to:

```text
bin
config
libs
licenses
LICENSE
NOTICE
```

---

# 4. Important Kafka Scripts

Check the Kafka scripts:

```bash
ls bin
```

Important scripts:

```text
kafka-server-start.sh
kafka-server-stop.sh

kafka-storage.sh

kafka-topics.sh

kafka-console-producer.sh
kafka-console-consumer.sh
```

These are the Linux versions of the Windows `.bat` commands.

---

# 5. Kafka 4.x KRaft Setup

Kafka 4.x uses **KRaft mode**, so storage needs to be initialized before starting Kafka.

Go to Kafka:

```bash
cd ~/kafka
```

Generate a cluster ID:

```bash
KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"
```

Check the generated ID:

```bash
echo $KAFKA_CLUSTER_ID
```

Format Kafka storage:

```bash
./bin/kafka-storage.sh format --standalone -t "$KAFKA_CLUSTER_ID" -c ./config/server.properties
```

If the command completes successfully, Kafka storage is ready.

---

# 6. Start Kafka Broker

Run:

```bash
cd ~/kafka
```

Start Kafka:

```bash
./bin/kafka-server-start.sh ./config/server.properties
```

Keep this terminal running.

Kafka should now be running on:

```text
localhost:9092
```

---

# 7. Open a Second Terminal

In GitHub Codespaces, open a new terminal.

Run:

```bash
cd ~/kafka
```

Check existing topics:

```bash
./bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
```

---

# 8. Create a Topic

Create the topic:

```bash
./bin/kafka-topics.sh \
  --create \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Check topics:

```bash
./bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

Expected:

```text
ashrit
```

---

# 9. Describe the Topic

To see topic details:

```bash
./bin/kafka-topics.sh \
  --describe \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

This shows information such as:

* Partition count
* Replication factor
* Leader
* Replicas
* ISR

---

# 10. Start Kafka Producer

In the second terminal:

```bash
cd ~/kafka
```

Start the producer:

```bash
./bin/kafka-console-producer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Now type messages:

```text
hello ashrit
kafka is working
this is my first message
```

Each line is sent as a separate Kafka message.

To stop the producer:

```text
Ctrl + C
```

---

# 11. Start Kafka Consumer

Open a third terminal.

Run:

```bash
cd ~/kafka
```

Start the consumer:

```bash
./bin/kafka-console-consumer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092 \
  --from-beginning
```

You should see messages such as:

```text
hello ashrit
kafka is working
this is my first message
```

The consumer will continue waiting for new messages.

Stop it with:

```text
Ctrl + C
```

---

# 12. Test Producer and Consumer Together

Keep the consumer running:

```bash
./bin/kafka-console-consumer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Open another terminal and run:

```bash
./bin/kafka-console-producer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Send:

```text
message 1
message 2
message 3
```

The consumer should receive them immediately.

---

# 13. Windows → Codespaces Command Mapping

The main difference is that Windows uses `.bat` files while Codespaces uses Linux `.sh` scripts.

## Start Kafka

### Windows

```powershell
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### Codespaces

```bash
./bin/kafka-server-start.sh ./config/server.properties
```

---

## Topics

### Windows

```powershell
.\bin\windows\kafka-topics.bat
```

### Codespaces

```bash
./bin/kafka-topics.sh
```

---

## Producer

### Windows

```powershell
.\bin\windows\kafka-console-producer.bat
```

### Codespaces

```bash
./bin/kafka-console-producer.sh
```

---

## Consumer

### Windows

```powershell
.\bin\windows\kafka-console-consumer.bat
```

### Codespaces

```bash
./bin/kafka-console-consumer.sh
```

---

# 14. Command Conversion Rule

Remember:

```text
Windows
.\bin\windows\xxxxx.bat

        ↓

Codespaces/Linux
./bin/xxxxx.sh
```

The Kafka concepts and most Kafka options remain the same.

For example:

```text
--topic
--create
--delete
--list
--describe
--bootstrap-server
--from-beginning
```

remain the same.

---

# 15. Complete Installation Commands

If setting up Kafka from scratch, these are the main installation commands:

```bash
sudo apt update

sudo apt install openjdk-17-jdk -y

cd ~

wget https://downloads.apache.org/kafka/4.0.0/kafka_2.13-4.0.0.tgz

tar -xzf kafka_2.13-4.0.0.tgz

mv kafka_2.13-4.0.0 kafka

cd ~/kafka

java -version
```

Generate the Kafka cluster ID:

```bash
KAFKA_CLUSTER_ID="$(./bin/kafka-storage.sh random-uuid)"
```

Format storage:

```bash
./bin/kafka-storage.sh format \
  --standalone \
  -t "$KAFKA_CLUSTER_ID" \
  -c ./config/server.properties
```

Start Kafka:

```bash
./bin/kafka-server-start.sh ./config/server.properties
```

---

# 16. Complete Topic Commands

Create:

```bash
./bin/kafka-topics.sh \
  --create \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

List:

```bash
./bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

Describe:

```bash
./bin/kafka-topics.sh \
  --describe \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Delete:

```bash
./bin/kafka-topics.sh \
  --delete \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

---

# 17. Complete Producer Commands

Start:

```bash
./bin/kafka-console-producer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Then enter messages:

```text
hello
kafka
ashrit
```

---

# 18. Complete Consumer Commands

Start:

```bash
./bin/kafka-console-consumer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

Read previous messages:

```bash
./bin/kafka-console-consumer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092 \
  --from-beginning
```

---

# 19. Check Whether Kafka Is Running

Check the process:

```bash
ps aux | grep kafka
```

You can also test the broker:

```bash
./bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --list
```

If the command successfully communicates with Kafka, the broker is running.

---

# 20. Stopping Kafka

If Kafka is running in the current terminal:

```text
Ctrl + C
```

You can also stop it using:

```bash
cd ~/kafka

./bin/kafka-server-stop.sh
```

---

# 21. Typical Workflow

Every time you want to work with Kafka:

### Terminal 1 — Kafka Broker

```bash
cd ~/kafka

./bin/kafka-server-start.sh ./config/server.properties
```

### Terminal 2 — Topic / Producer

```bash
cd ~/kafka

./bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

Then:

```bash
./bin/kafka-console-producer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092
```

### Terminal 3 — Consumer

```bash
cd ~/kafka

./bin/kafka-console-consumer.sh \
  --topic ashrit \
  --bootstrap-server localhost:9092 \
  --from-beginning
```

---

# 22. AIOps Project Usage

For an AIOps project, Kafka can be used to continuously collect operational metrics.

Example:

```text
System / Application
        │
        │ CPU
        │ Memory
        │ Disk
        │ Logs
        ↓
     Kafka
        │
        │ topic
        ↓
 system-metrics
        │
        ↓
    Airflow
        │
        ↓
 Preprocessing
        │
        ↓
Anomaly Detection
        │
        ↓
 Alert / Dashboard
```

Example message:

```json
{
  "cpu": 85,
  "memory": 72,
  "disk": 91
}
```

Kafka stores and distributes these events through the topic.

---

# 23. Important Notes

### Kafka broker address

Use:

```text
localhost:9092
```

not just:

```text
localhost
```

Example:

```bash
--bootstrap-server localhost:9092
```

### Kafka terminal

When running:

```bash
./bin/kafka-server-start.sh ./config/server.properties
```

keep that terminal open while using Kafka.

Use additional Codespace terminals for producers, consumers, and topic commands.

### KRaft

Kafka 4.x uses KRaft instead of requiring a separate ZooKeeper setup.

Therefore, the storage-formatting step is required for a fresh installation.

---

# 24. Quick Cheat Sheet

```bash
# Go to Kafka
cd ~/kafka

# Start Kafka
./bin/kafka-server-start.sh ./config/server.properties

# List topics
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Create topic
./bin/kafka-topics.sh --create --topic ashrit --bootstrap-server localhost:9092

# Describe topic
./bin/kafka-topics.sh --describe --topic ashrit --bootstrap-server localhost:9092

# Producer
./bin/kafka-console-producer.sh --topic ashrit --bootstrap-server localhost:9092

# Consumer
./bin/kafka-console-consumer.sh --topic ashrit --bootstrap-server localhost:9092

# Consumer from beginning
./bin/kafka-console-consumer.sh --topic ashrit --bootstrap-server localhost:9092 --from-beginning

# Stop Kafka
./bin/kafka-server-stop.sh
```

---

# 25. Final Working Setup

After successful installation:

```text
GitHub Codespace
│
├── ~/kafka
│   │
│   ├── bin/
│   │   ├── kafka-server-start.sh
│   │   ├── kafka-topics.sh
│   │   ├── kafka-console-producer.sh
│   │   └── kafka-console-consumer.sh
│   │
│   └── config/
│       └── server.properties
│
└── Kafka Broker
        │
        └── localhost:9092
              │
              └── ashrit
                   │
             ┌─────┴─────┐
             ↓           ↓
```
