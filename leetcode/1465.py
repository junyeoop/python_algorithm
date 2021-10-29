class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # add the start and end cut, then sort
        horizontalCuts.append(0)
        horizontalCuts.append(h) 
        horizontalCuts.sort()
        hor_cut = horizontalCuts
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        ver_cut = verticalCuts
        
        # find the maximum value between the cuts
        max_h = 0
        max_w = 0
        
        for i in range(1, len(hor_cut)):  # horizontal
            max_h = max(max_h, hor_cut[i]-hor_cut[i-1])
        
        for j in range(1, len(ver_cut)):  # vertical
            max_w = max(max_w, ver_cut[j]-ver_cut[j-1])
        
        # return the product of max_h and max_w mod (10^9+7)
        return (max_h * max_w) % (1_000_000_000 + 7)
