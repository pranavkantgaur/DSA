# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello wor
#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        # 1. sort jobs based on deadline
        # 2. sort based on profit
        # 3. for each deadline select the job with max profit, add profit , job count
        # 4. return job profit and job count
        # <deadline: [profit_i]>
        print(sorted(Jobs, key = lambda job:job[2], reverse=True))
        n_jobs = 0
        profit = 0
        jobs_aux = sorted(Jobs, key = lambda job: job[2], reverse=True)
        curr_time = 0
        for job in jobs_aux:
            if curr_time + 1 <= job[1]: # job is feasible?
                profit += job[2]
                n_jobs += 1
            curr_time += 1
        return n_jobs, profit    
            
        
        


Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
n = 5
sol = Solution()
print(sol.JobScheduling(Jobs, n))
