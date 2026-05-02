class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_count = Counter(nums)
        
        
        top_k_elements = [item for item, count in freq_count.most_common(k)]
        
        return top_k_elements
            

 
        


