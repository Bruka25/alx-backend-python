The following python codes are for ALX 0x02-python_async_comprehension project for the alx-backend-python, inside it contains the following python codes:

* A coroutine called async_generator that takes no arguments
  Coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10

* Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments
  Coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers

* Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times  in parallel using asyncio.gather
  Measure_runtime should measure the total runtime and return it
  Notice that the total runtime is roughly 10 seconds, explain it to yourself  
