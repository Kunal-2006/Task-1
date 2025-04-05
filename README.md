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
     Used Linux Terminal commands by which the desired output was found.
  2. Question 2
     Used Bash coding for coding the required and desired commands. 
 #### 2. Medium Dose
  1. Question 1
      
  3. Question 2
  4. Question 3
     
  5. Question 4
    
    
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

    Sanchiko filter = Median of 3 values
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

    ####Apply filters
    muchiko_filter = muchiko(data)
    sanchiko_filter = sanchiko(data)

    ####Print individual filter results
    print("Muchiko Filter:")
    for d in muchiko_filter:
      print(d)

    ####print("Sanchiko Filter:")
    for d in sanchiko_filter:
      print(d)

    Hybrid 1 = Sanchiko(Muchiko(data))
    hybrid1 = sanchiko(muchiko_filter)
    print("Hybrid 1 (Sanchiko on Muchiko):")
    for d in hybrid1:
      print(d)

    Hybrid 2 = Muchiko(Sanchiko(data))
    hybrid2 = muchiko(sanchiko_filter)
    print("Hybrid 2 (Muchiko on Sanchiko):")
    for d in hybrid2:
    print(d)

  5. Question 5   

    Function to convert Euler angles (yaw, pitch, roll) to quaternion
    import math
    def quaternion(yaw, pitch, roll):
    #### Convert degrees to radians
    yaw_rad = math.radians(yaw)    ### Rotation around z-axis
    pitch_rad = math.radians(pitch) ### Rotation around y-axis
    roll_rad = math.radians(roll)  ### Rotation around x-axis
    
    ### Half-angles for quaternion formula
    cy = math.cos(yaw_rad / 2)    ### Cosine of yaw/2
    sy = math.sin(yaw_rad / 2)    ### Sine of yaw/2
    cp = math.cos(pitch_rad / 2)
    sp = math.sin(pitch_rad / 2)
    cr = math.cos(roll_rad / 2)
    sr = math.sin(roll_rad / 2)
    
    ### Quaternion components (w, x, y, z)
    w = cr * cp * cy + sr * sp * sy  /// Real part
    x = sr * cp * cy - cr * sp * sy  ### x-axis component
    y = cr * sp * cy + sr * cp * sy  ### y-axis component
    z = cr * cp * sy - sr * sp * cy  ### z-axis component
    
    ### Return as list, rounded for clarity
    return [round(w, 4), round(x, 4), round(y, 4), round(z, 4)]

    ### Test the function
    yaw = 0    ### Example: no rotation
    pitch = 0
    roll = 0
    result = quaternion(yaw, pitch, roll)

    ### Print results
    print("Converting Earth Rotation to Martian Quaternion:")
    print(f"Input (Yaw, Pitch, Roll): ({yaw}°, {pitch}°, {roll}°)")
    print(f"Quaternion [w, x, y, z]: {result}")

    ### Additional test with rotation
    yaw_test = 90  # 90° yaw
    pitch_test = 0
    roll_test = 0
    result_test = quaternion(yaw_test, pitch_test, roll_test)
    print("\nTest with 90° Yaw:")
    print(f"Input: ({yaw_test}°, {pitch_test}°, {roll_test}°)")
    print(f"Quaternion [w, x, y, z]: {result_test}")
    print("Brick is ready for Mars with Muchiko and Sanchiko!")
  #### 3. Hard Dose
  1. Question 1
  2. Question 2
  3. Question 3

## Learning Experience-->
  I had a very good experience solving the task 1 for me though it was very challenging at the start but with time and logic it became easy leaving some questions.
  I have learnt a lot of new things and also gained some new perspectives. Doing the task 0 and task 1 was a lot fun by these tasks I again relearnt python which     i had forgotten since I learned when I was in 11-12th std.
## Theorams,Equations,Sketches used for solving the problems-->

## Challenges Faced-->
  Initially due to some pc error I couldn't dual boot laptop even after spending nights to do it I couldn't but later somehow I did it.
    The task 1 light dose I hadn't studied bash or Linux  I had forgotten python and didn't know open cv and how to apply bfs,dijakstra for the navigation       
    question and also I didn't know GitHub. But with spending time watching videos on these topics reading from blogs and using ai tools to fins the theory on         particular questions it helped me understand these topics and hence I could solve majority questions of the task.
## Explain your Approach-->
   My approach was that during the initial days of task 1 I had discussed all questions with my friend which was like a overview and what i did was I would           first explore the links provided in document and see the videos and blogs related to it and see the cheat sheets of Linux and bash for the light dose
    And finsihed the light dose.Then I started hard dose where what I used to do is like in 1 question I put Grid mapping in youtube  and later I saw videos on        BFS matrix type of questions and also some of dijasktras.Also in the other hard dose question I had totally searched video on yt and if I couldn't find videos      on YT I just put the question  on grok from where it gave prompt to recieve yt video recommendations for each question to understand the theory. For medium       dose question almost all questions were easy since it was like done some questions like q-5 which I had no knowledge upon upon surfing I got the formula and       later used it for coding.
## Resources Used-->
  Used a lot YT videos which came a lot use 

