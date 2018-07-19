/*
SerialGraphing.pde

Mohamed Ebsim

Contqact Jesse Rogerson, @ jrogerson@ingeniumcanada.org

Originally created on Jully 13, 2018
-------------------------------------

This program is a quick way of looking at changing data
as it comes in from the arduino. Using processing, the
data is graphed and is updated continously.

-------------------------------------

Resources Used:

https://www.arduino.cc/en/Tutorial/Graph

*/

// Libraries
import processing.serial.*;
import java.util.Queue;
import java.util.LinkedList;

// Creating variables.
Serial port;
int x;
float input;
Queue<Float> inputs; 	// A queue was used since then the bar would be continously moving left as
						// new data comes in on the right, and old data disappears on the left
Queue<Float> inputsCopy;

/*
Setup method is run once, when the program is started. It
initializes the variables and sets some preferences for the
window that will be displayed.
*/
void setup() {
	// Set size of window
	size(1000,800);

	// Initialize variables
	port = new Serial(this, Serial.list()[1], 9600); // Telling the variable the port and the speed
	port.bufferUntil('\n'); // Telling it that new data ends with '\n'
	inputs = new LinkedList();
	x = 1;
	input = 0;

	// Set background black
	background(0);

}

/*
This method controlls what is drawn onto the window. It clears
and redraws a bar graph of the data over time.
*/
void draw() {
	// Sets the colour for the lines blue
	stroke(0, 0, 255);

	// Resets the x count to 0
	x = 0;

	// Clears screen
	background(0);

	// Duplicates list in order to prevent concurent modification error
	inputsCopy = new LinkedList(inputs);

	// Checks if list is not empty
	if(inputsCopy.peek() != null) {

		// Loops through every item in the list
		for(Float in:inputsCopy) {

			// Sets the height of the graph (show differences more accurately by showing a smaller range)
			float y = in - 20;
			y *= 10;

			// Draws rectangles at different spots along the bar with width 5
			rect(x*6, 150, 5, -y);

			// Increases the x count so the next item is at a different position
			x++;
		}
	}

	// For debugging purposes, outputs the list
	println(inputsCopy);
}

/*
This method is used to read data that is comming in via serial
transmisiion. It reads the data, and manages the list of data. 
*/
void serialEvent(Serial port) {
	// Reads in what is coming via the port
	String inString = port.readString();

	// Continues if the string is not empty
	if(inString != null) {
		// Removes an item if the list of items has hit a certain point (currently set to 15 seconds of data)
		if(inputs.size() >= 60) {
			inputs.remove();
		}

		// Converts the input to a number
		input = float(inString);

		// If the input is not not a number, then it adds it to the list
		// Prevents improper reading in the first transmissions
		if(!Float.isNaN(input)) {
			inputs.add(input); 
		}
	}
}
