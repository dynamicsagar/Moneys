### **Framework Documentation**

The main objectives in functional automation testing of the API are: 
1. To ensure that the implementation is working correctly as expected — no bugs!
2. To ensure that the implementation is working as specified according to the requirements specification.
3. To prevent regressions between code merges and releases.

##### API Test Action
Below are the  individual actions we will take as per API test flow. For each API request, the test would need to take the following actions: 
1. **Verify correct HTTP status code**. For example, creating a resource should return 201 CREATED and unpermitted requests should return 403 FORBIDDEN, etc.
2. **Verify response payload**. Check valid JSON body and correct field names, types, and values including in error responses.
3. **Verify response headers**. HTTP server headers have implications on both security and performance.

## Usage

### Installation

```python

pip3 install silasdk

```
## Install requirements
Install additional requirements from requirements.text.

## Packages for framework

## Packages : 
We have separate packages for test, utility and testdata, All tests related classes come under Tests Package.

## Utility Class
Utility class stores and handles the functions (The Code which is repetitive in Nature Such as accessing excels, getuniquename, statuscode etc..) Which can be commonly used across the framework. The reason behind creating a utility class is to achieve reusability .

## Test Data 
All the historical test data will be kept in excel sheet(silamoney.xlsx), we pass test data and handle data driven testing. We use python libraries to handle excel sheets.

## Pytest 
This will be used for Assertions,Grouping and Parallel execution.

## Version Control Tool 
we use 1 as a repository to store our tests scripts.

## Jenkins
By using Jenkins CI (Continuous Integration) Tool, We execute test cases on daily and for Nightly execution based on the schedule.Test Result will be sent to the peers using Jenkins.

##Extent Reports 
For the reporting purpose, we are using extent reports. it generates beautiful HTML reports. we use the extent reports for maintaining logs and to include the screenshots of failed test cases in the Extent Report
