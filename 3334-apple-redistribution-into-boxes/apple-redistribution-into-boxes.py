class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple=sum(apple)
        capacity.sort(reverse=True)

        used=0
        bag=0

        for i in capacity:
            used+=i
            bag+=1

            if(used>=total_apple):
                return bag

        