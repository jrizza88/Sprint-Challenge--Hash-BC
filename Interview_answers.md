## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
- The runtime complexity to add to the front of an array array of O(n) because you would have to loop through the array and push all the contents to the right by one in order to allocate for space in the front of the array. Remaining n-1 elements are moved up.
- The runtime complexity to add to the back of an array array of O(1) because it is a fast and immediate input that does not require counting through your arrays or requiring any sort of loop in order to add it to the rear. This operation will always take same time.
- The runtime complexity for both removing from the front of a dynamic array is O(n) . This is because a search is being done on the dynmaic array and each element has to be moved over by one space. 
- The runtime complexity for both removing from the back of a dynamic array is O(1) . This is because it is the last element of the array and no other elements have to move their positions. 

* What is the worse case scenario if you try to extend the storage size of a dynamic array?
- The worst case scenario would be O(n). This is because you have to allocate additional space/memory block in order to grow the array. 

* Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
- Blocks are individual links of the chain. It is digital information. Blocks are structured by index numbers, timestamps, list of transactions, proofs that are used to mine a block and crytopgraphic hases of previous blocks.
- The chain is a public database.
- The data is organized by being packaged into blocks, which is then linked to a chain with other blocks of similar information. 

* Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
- Proof of work is what helps to prevent hackers from being successful in the completion of attacking the blockchain system. You can use something like a SHA-256 (SHA = Secure Hash Algorithm) hashing function to create a hash of the last block concatenated with the proposed solution. First N characters must be zero.  A proof of work requires each individual block to be edited after, which takes a long time to process. With each solution requiring the use of the hash of the previous block, plus a new value, it means that you cannot plan ahead nor can you reuse it, which leads to many proofs having to be done. This helps to make it difficult to generate a new block. Essentially, the block chain carries new records with a unique history. 
