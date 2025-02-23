# Project Description

This project contains a `dataset` folder, which stores 190 examples related to test cases. Each example includes the generated initial test cases and different test case sets.

## Folder Structure

### The `dataset` Folder
The `dataset` folder is the root directory of all test case data, containing 190 sub - folders. Each sub - folder represents an example of a test case.

### Folder Structure of a Single Example
Each example's folder contains the following:

#### Initial Test Case Files
- **testcase.txt**: Stores the initial test cases generated by KLEE.
- **testcase_our.txt**: Stores the initial test cases supplemented by our method based on testcase.
- **testcase_KLEE.txt**: Stores the initial test cases generated in a random way based on testcase.

#### Test Case Set Folders
- **ALLSet**: This folder contains the test case sets with full permutations.
- **GmSet**: Contains the test case sets generated using Gm.
- **RandomSet**: Contains the test case sets generated by random sorting.
