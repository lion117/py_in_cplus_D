python commercial project

this project 's main purpose is to make all steps of python embed C++ fluent
ok let's make a plan for this project
1	MFC have button to trigger the python function
2	function will trigger python function which will calling the qt gui
3	qt gui have a button which could calculate two word plus and give the answer
4	when i close the function , if in debug statue , the python will
	distribute the python files together
	one thing have bother me whether the distribute function should be
	in the file or just stand alone




/////////////////////////////////////////////////////////////////////////
// debug and analysis
1	generally speaking , the most potential threaten is from the distribute
	i have no idea how did work .if i don't embed this file into the current
	file , i don't kwon what will happen . the good news is that i could
	optimize it after i had learn something from distribute on how to distribute
	the files .
	or i could choose test it in different environment to make sure it wil
	work

2	now it is time to build up the base software

3   to management the python files , i think the python files should not be the same folder , it should be the sub folder . it's more easy for management

4   for the py entrance , i think i should provide a entrance function for test and for the c++

5   fist thing i should design the base qt gui for test . python embed function stay in the function layer data communication all the data should stay in the entrance . there need i build up a message port for the python response. or i just new a thread for that

6	i am worried about if i set the project huge , whether i will have enough 
	time to do other things . there are all important for me . i need do the 
	little module first . and then i will take the night time to accomplish the 
	rest 
	
7	i think i am lack the base thrown and accept exception ability which i will 
	need spend some time to stress it 
	
8	 when i take the throw exception , if it is cout , the software will do 
	nothing . 
	
9	i think the base function have been realized . it is turn for the distribute 
	and release the python 
	
10	 when the software is closed , the console prompt memory leak . 

11	 the first structure only could change when i take used it . after i 
	distribute it . nothing i could do until i learn how to use of distribute 
	library 
	
12	the next step is to distribute the function in debug and specified 
	the the folder to copy file into 
	i am curious if the distribute function is not stay with the 
	
13	i think i had better change my strategy to test the distribute 
	there is no necessary to involved the c++ compiler . 
	i will left this project tomorrow . now i would like to take the java 
	project 





