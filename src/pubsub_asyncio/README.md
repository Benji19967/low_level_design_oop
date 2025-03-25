# Designing a pubsub system

https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/pub-sub-system.md

## Requirements

1. The Pub-Sub system should allow publishers to publish messages to specific topics.
2. Subscribers should be able to subscribe to topics of interest and receive messages published to those topics.
3. The system should support multiple publishers and subscribers.
4. Messages should be delivered to all subscribers of a topic in real-time.
5. The system should handle concurrent access and ensure thread safety.
6. The Pub-Sub system should be scalable and efficient in terms of message delivery.


# Things to remember

1. There is no limitation in the number of tasks created --> I can have unlimited number of subscribers
    - When using threads, limited to roughly 2000 threads/subscribers with the current implementation
2. You need to make sure the solution scales with the number of messages sent as well as with the number of subscriptions
    - Seperate the tasks that listen to topics to fetch work and tasks that actually do the work --> can have many more tasks
    running simultaneously