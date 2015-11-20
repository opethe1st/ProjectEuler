__author__ = 'Opemipo'



Stats = {0:set([]),1:set([]),2:set([]),3:set([]),4:set([]),5:set([]),6:set([]),7:set([]),8:set([]),9:set([])}
f = open("input","r")

entry = f.readline()
while entry is not '':

    nums = map(int,list(entry)[:-1])
    #print nums
    Stats[nums[0]].add(nums[1])
    Stats[nums[0]].add(nums[2])
    Stats[nums[1]].add(nums[2])
    entry = f.readline()

print Stats