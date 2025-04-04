# Software Task-1
## Mars_Task 1 submission by Kunal Garag ME24I1022
### **Table of Contents** 
#### 1. Learning Experience
#### 2. Theorams,Equations,Sketches used for problem solving
#### 3. Challenges faced
#### 4. My Approach
#### 5. Resources Used
#### 6. Task Solutions
#### 1. Light Dose
  1. Question 1
  2. Question 2
 #### 2. Medium Dose
  1. Question 1
  2. Question 2
  3. Question 3
  4. Question 4
    
    //
       file = open("log.txt", "r")
      data = []
      for line in file:
      if line.strip():
        data.append(float(line.strip()))
      file.close()
      *Muchiko filter = Moving Average of 3 values*
      def muchiko(data):
        result = []
        n = len(data)
        for i in range(1, n - 1):
          a = data[i - 1]
          b = data[i]
          c = data[i + 1]
        avg = (a + b + c) / 3
        result.append(avg)
        return result

    // Sanchiko filter = Median of 3 values
    def sanchiko(data):
      result = []
      n = len(data)
      for i in range(1, n - 1):
        a = data[i - 1]
        b = data[i]
        c = data[i + 1]
        values = [a, b, c]
        values.sort()
        median = values[1]
        result.append(median)
    return result

    // Apply filters
    muchiko_filter = muchiko(data)
    sanchiko_filter = sanchiko(data)

    // Print individual filter results
    print("Muchiko Filter:")
    for d in muchiko_filter:
      print(d)

    print("Sanchiko Filter:")
    for d in sanchiko_filter:
      print(d)

    // Hybrid 1 = Sanchiko(Muchiko(data))
    hybrid1 = sanchiko(muchiko_filter)
    print("Hybrid 1 (Sanchiko on Muchiko):")
    for d in hybrid1:
      print(d)

    // Hybrid 2 = Muchiko(Sanchiko(data))
    hybrid2 = muchiko(sanchiko_filter)
    print("Hybrid 2 (Muchiko on Sanchiko):")
    for d in hybrid2:
    print(d)

  6. Question 5
  #### 3. Hard Dose
  1. Question 1
  2. Question 2
  3. Question 3

## Learning Experience-->
## Theorams,Equations,Sketches used for solving the problems-->
## Challenges Faced-->
## Explain your Approach-->
## Resources Used-->

