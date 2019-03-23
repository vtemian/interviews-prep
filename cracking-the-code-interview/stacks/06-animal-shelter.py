import time
from typing import Union


DOG = 'dog'
CAT = 'cat'


class AnimalShelter:
    def __init__(self):
        self.queues = {
            DOG: [],
            CAT: [],
        }

    def enqueue(self, animal_type: str, animal: str) -> bool:
        if animal_type not in self.queues:
            return False

        self.queues[animal_type].append({
            'when': int(time.time()),
            'animal': animal
        })

        return True

    def dequeue_any(self) -> str:
        when = animal = min_queue = None

        for queue in self.queues.values():
            if not queue:
                continue

            new_when, new_animal = queue[0].values()
            if not when or new_when < when:
                when = new_when
                animal = new_animal
                min_queue = queue

        if not min_queue:
            return None

        min_queue.pop(0)['animal']
        return animal

    def _dequeue(self, animal_type: str) -> Union[None, str]:
        queue = self.queues.get(animal_type)
        if not queue:
            return None

        return queue.pop(0)['animal']

    def dequeue_dog(self) -> Union[None, str]:
        return self._dequeue(DOG)

    def dequeue_cat(self) -> Union[None, str]:
        return self._dequeue(CAT)


for use_case, expected_result in [
        (
            [('enqueue', CAT, 'cat'), ('enqueue', DOG, 'dog'), ('enqueue', '1', 'b'), ('dequeue_cat', ), ('dequeue_any', )],
            [True, True, False, 'cat', 'dog']
        ),
]:
    stack = AnimalShelter()

    result = [
        getattr(stack, method)(*arguments)
        for method, *arguments in use_case
    ]
    assert result == expected_result, "{} != {}".format(result, expected_result)
