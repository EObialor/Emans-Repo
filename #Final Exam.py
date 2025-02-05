#Final Exam 
'''

This program will exract integers from a string of characters and return them in standard output 

'''




def extractintegers(final_exam_string):
    integers = []
    current_int = "" 
    
    #Run through each character in the string
    for char in final_exam_string:
        if char.isdigit(): 
            current_int += char 
        elif current_int:
            integers.append(int(current_int))
            current_int = "" 
   
    if current_int:
        integers.append(int(current_int))
    
    return integers

def listsort(integers):
    integers.sort(reverse=True)
    print(integers)

def main():
    final_exam_string = "2 Happy 60 To End 7 This 8 Semester 54"
    
    integers = extractintegers(final_exam_string)
    
    listsort(integers)


if __name__ == "__main__":
    main()
