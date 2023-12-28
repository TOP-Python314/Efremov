def central_tendency(n1: float, n2: float, /, *args) -> dict:
    nums = sorted([n1, n2, *args])
    
    if len(nums) % 2 == 0:
        median = (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2
    else:
        median = nums[len(nums)//2]
        
    arithmetic = sum(nums)/len(nums)
    
    geometric = 1
    for i in nums:
        geometric *= i**(1/len(nums))
        
    harmonic = len(nums) / sum([1/i for i in nums])
    print({'median': median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic})
    
# >>> central_tendency(23, 17, 46, 4, 6)
# {'median': 17, 'arithmetic': 19.2, 'geometric': 13.397666598648394, 'harmonic': 9.24714229404809}

# >>> sample = [10, 30, 50, 70, 90]
# >>> central_tendency(*sample)
# {'median': 50, 'arithmetic': 50.0, 'geometric': 39.36283427035354, 'harmonic': 27.97513321492007}
