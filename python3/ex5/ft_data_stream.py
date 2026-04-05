import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep",
           "grab", "move", "climb", "swim", "release", "use"]


def gen_event() -> typing.Generator:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(events) -> typing.Generator:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        events.pop(index)
        yield event


print("=== Game Data Stream Processor ===")

generator = gen_event()
for i in range(1000):
    name, action = next(generator)
    print("Event " + str(i) + ": Player " + name + " did action " + action)

event_list = []
generator2 = gen_event()
for i in range(10):
    event_list.append(next(generator2))
print("Built list of 10 events:", event_list)

for event in consume_event(event_list):
    print("Got event from list:", event)
    print("Remains in list:", event_list)
