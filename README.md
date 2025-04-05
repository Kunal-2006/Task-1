# Software Task-1
## Mars_Task 1 submission by Kunal Garag ME24I1022
### **Table of Contents** 
#### 1. Learning Experience
#### 2. Theorams,Equations,Sketches used for problem solving
#### 3. Challenges faced
#### 4. My Approach
#### 5. Resources Used
#### 6. Task Solutions
## Learning Experience-->
  I had a very good experience solving the task 1 for me though it was very challenging at the start but with time and logic it became easy leaving some questions.
  I have learnt a lot of new things and also gained some new perspectives. Doing the task 0 and task 1 was a lot fun by these tasks I again relearnt python which     i had forgotten since I learned when I was in 11-12th std.
## Theorams,Equations,Sketches used for solving the problems-->
Medium Dose Task 5: Quaternion Conversion
Converts Earth’s Euler angles (yaw, pitch, roll) to Martian quaternions for Rover Brick.

4. **Quaternion Components**  
   - **Formulas**:  
     - `w = cos(y/2) * cos(p/2) * cos(r/2) + sin(y/2) * sin(p/2) * sin(r/2)`  
     - `x = sin(r/2) * cos(p/2) * cos(y/2) - cos(r/2) * sin(p/2) * sin(y/2)`  
     - `y = cos(r/2) * sin(p/2) * cos(y/2) + sin(r/2) * cos(p/2) * sin(y/2)`  
     - `z = cos(r/2) * cos(p/2) * sin(y/2) - sin(r/2) * sin(p/2) * cos(y/2)`  
   - **Variables**:  
     - `y`: Yaw (z-axis rotation, degrees, converted to radians).  
     - `p`: Pitch (y-axis rotation, degrees, converted to radians).  
     - `r`: Roll (x-axis rotation, degrees, converted to radians).  
   - **Example (yaw = 90°, pitch = 0°, roll = 0°)**:  
     - Half-angles: `  
     - `w = cos(45°) * cos(0°) * cos(0°) + sin(45°) * sin(0°) * sin(0°) =
     - `x = sin(0°) * cos(0°) * cos(45°) - cos(0°) * sin(0°) * sin(45°) = 
     - `y = cos(0°) * sin(0°) * cos(45°) + sin(0°) * cos(0°) * sin(45°) = 
     - `z = cos(0°) * cos(0°) * sin(45°) - sin(0°) * sin(0°) * cos(45°) = 
   - **Purpose**: Converts 3D rotations to quaternions, avoiding gimbal lock.

## Challenges Faced-->
  Initially due to some pc error I couldn't dual boot laptop even after spending nights to do it I couldn't but later somehow I did it.
    The task 1 light dose I hadn't studied bash or Linux  I had forgotten python and didn't know open cv and how to apply bfs,dijakstra for the navigation       
    question and also I didn't know GitHub. But with spending time watching videos on these topics reading from blogs and using ai tools to fins the theory on         particular questions it helped me understand these topics and hence I could solve majority questions of the task.
## Explain your Approach-->
   My approach was that during the initial days of task 1 I had discussed all questions with my friend which was like a overview and what i did was I would           first explore the links provided in document and see the videos and blogs related to it and see the cheat sheets of Linux and bash for the light dose
    And finsihed the light dose.Then I started hard dose where what I used to do is like in 1 question I put Grid mapping in youtube  and later I saw videos on        BFS matrix type of questions and also some of dijasktras.Also in the other hard dose question I had totally searched video on yt and if I couldn't find videos      on YT I just put the question  on grok from where it gave prompt to recieve yt video recommendations for each question to understand the theory. For medium       dose question almost all questions were easy since it was like done some questions like q-5 which I had no knowledge upon upon surfing I got the formula and       later used it for coding and with the help of AI tools aai tools rmeoved my syntax errors.
## Resources Used-->
  Used a lot YT videos which came to a lot use AI tools also.
#### 1. Light Dose
  1. Question 1
     Used Linux Terminal commands by which the desired output was found.
  2. Question 2
     Used Bash coding for coding the required and desired commands. 
 #### 2. Medium Dose
  1. Question 1
       
  2. Question 2
             Here in this question we have used python to solve the program by first creating an dictionary of the all the               morse code alphabets where the key in morse code alphabets and item is the english alphabets.
     1. Step-1 So we have an file named as Morse.txt which will be opening and for the data in the file we first read the                  whole code and also strip the spaces which occur between the characters.
     2. Step-2 We will now first close the file since saved all the data and then split the data in words by split function                 and then with help of split function to split the letters from each other.
     3. Step-3 With the help of the for loop we will take the item according to the morse code key and append th english                   alphabet into a empty list and that is th final code needed.
     
  3. Question 3
           Here in this question I have used Pyhton to solve the problem statement created an string where the data is present and also a new list where all the data will be stored.
     1. Step-1
         using for loop we see each index of the string and and shift the value by first gettting ascii value and then               decreasing the value bu there might be a chance A might be decreased by 1 so we use the second loop to change           the index of ascii and then when subtraction is done intended result is accomplished.
     2. Step-2
         The data is is then appended in the list new.
  4. Question 4
         Here in the problem statement we have again used Pyhton programming language.
       1. Step-1
         first we will open log.txt as said in the question using r mode which is the read mode and create an empty list data where we will again like earlier strip the file to remove the sapces adn then store all data of the log.txt in data list.
        2. Step-2
          We will now define Muchiko who just finds the avg of data in the list data and append the avg in result list which is created before.
         3. Step-3
           We will now define Sanchiko who takes data and then sorts the data according to the numerical order then find the median of the 3 values in list and prints the value.
          4. Step-4
            We can create some hybrids like Sanchiko of Muchiko filter whih first find the avg of the values and then finds 3 averages and appends in the list which is when put in to Sanchiko filter where the again the avg list is sorted and now the values are arranged and the median value is given output.
          5. Step-5
             We can  create one more hybrid where first we can take the medians by arranging the numbers and then finsing the median and after finding the median the avg is found directly this is called Muchiko sanchiiko Hybrid.
     Out of these Sanchiko(muchiko filter is the best hybrid since it gives best balance of spike protection and smoothing.
  5. Question 5
         Here in the problem statement again pyhton programming language is used where
     1. Step-1
       The values of yaw,ptch,roll are taken from the user who has used the function from where first the angle is converted to radians.
     2. Step-2
       We will find the variables values needed foe the quaternion formula.
     3. Step-3
       We will find the values of w,x,y,z the 4 axis system has been calculated by the operation of the                 variables.
     
      
  #### 3. Hard Dose
  1. Question 1 For question 1 open a file and get the valued of row clumn obstacles and matrix order and create the grid form that part make queue for enetring the valueson which step is taken and keep adding the value sin queue till the final destination is reavhed. We are using BFS to do this code.
  2. For travelling use the method of direction ratios such that movement can be done 1 at atime and also keep a track of the blocks if there are in matrix,not on obstacles and also dont visit the visted blocks too.
  3. Question 2
     1. Step 1
        Import Libraries necessary for the task such as math module,cv2 module and numpy and module and name it as np for easier usage.
      2. Step 2
         Create an function to detect the arrow which has been used so for that first convert the image to grayscale since it helps to do easy processing and also we will be applying gausian blur to reduce noise and smooth edges.
      3. Step 3
           Use Canny Edge detector to find the contour the shpaes similar to required arrow shape and apply the polygon with 7 sided since the arrow contains of 7 vertices and then if found an 7 vertice polygon assume it to be an arrow and create an bounding rectangle arounfd it .
      4. Step 4
            Now by distance function we want to calculate its distance from the camera so for that we must first now the focal length formula and also the distance formula for that we will be entering the width of the arrow in the photo ad actualwidth_px and save the 17cm as real arrow width and also make the FOV as 55 degree.
       5. Step 5
              By using the formulas of Diagonal resolution ,focal length find the distance formula but first convert all the angle which is degree to radian by using math 
  4. Question 3
           Understood how fall back and sequence node work ,fall back node works will stop when next child gets to be successful if not successful then it will be a failure.
           Understood that Wequence Node works as if it just stops at first child if bwing success or failure.
#Participation in Maze rover competition
the competition is very good though there were less people than expected though i coudnt understand what was going something womething i knew which ingnited sparks for me take inrtrest in ROS more.Though we were the team with least duration of getting out of the maze by ourselves manually autonmaous mode was very bad for use since we didnt know any thing about it.

