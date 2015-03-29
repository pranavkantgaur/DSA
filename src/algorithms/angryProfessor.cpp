#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
      
    int nTestCases, totalNumberOfStudents, studentThreshold, totalInTimeStudents, arrivalTime;
        
    cin >> nTestCases;
    
    if (!(nTestCases >= 1 && nTestCases <= 10))
        exit(0);
    
    for (int testCaseID = 0; testCaseID < nTestCases; testCaseID++)
        {
            cin >> totalNumberOfStudents;
            cin >> studentThreshold;
        
            if (!(totalNumberOfStudents >= 1 && totalNumberOfStudents <= 1000 && studentThreshold >= 1 && studentThreshold <= totalNumberOfStudents))
                exit(0);                    
            
	    totalInTimeStudents = 0;
            for (int studentID = 0; studentID < totalNumberOfStudents; studentID++)
            {

    
		if ((totalNumberOfStudents - studentThreshold) < (studentID - totalInTimeStudents))
                    break;

   
                cin >> arrivalTime;
                
                if (abs(arrivalTime) > 100)
                    exit(0);
                
                if (arrivalTime <= 0)
                {
                    totalInTimeStudents++;
                    if (totalInTimeStudents >= studentThreshold)
                        break;                    
                }



             }
            
            if (totalInTimeStudents < studentThreshold)
                cout << "YES" << "\n";
            else
                cout << "NO" << "\n";
        }
    
    
     
        
    return 0;
}

