from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  swapped = True
  start = 0
  end = len_numbers - 1
  while swapped:
    swapped = False
    #右向き
    for i in range(start, end):
      if numbers[i] > numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        swapped = True
    if not swapped:
      break

    swapped = False
    end = end - 1
    #udemy 6:50から詳しい説明、要するにfor文が動く値をこのsortに合わせて決めているだけ
    #３からー１までー１ずつ動くということは３，２，１，０ということ。PHPでいう for($i=3;$i>-1;$i--)こんな書き方できるか
    #知らないけれど
    #左向き
    for i in range(end-1, start-1, -1):
      if numbers[i] > numbers[i+1]:    
          numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
          swapped = True

    start = start + 1 

  return numbers

if __name__ == '__main__':
  import random
  nums = [ random.randint(0, 1000) for i in range(10)]
  print(cocktail_sort(nums))          