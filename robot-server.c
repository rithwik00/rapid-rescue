/*
*****************************************************************************************
*
*        		===============================================
*           		Rapid Rescuer (RR) Theme (eYRC 2019-20)
*        		===============================================
*
*  This script is to implement Task 1B of Rapid Rescuer (RR) Theme (eYRC 2019-20).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
*/

/*
* Team ID:			[ Team-ID ]
* Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
* Filename:			task_1a.py
* Functions:		readImage, solveMaze
* 					[ Comma separated list of functions in this file ]
* Global variables:	CELL_SIZE
* 					[ List of global variables defined in this file ]
*/


// Include necessary header files
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



// Constants defined
#define SERVER_PORT 3333
#define RX_BUFFER_SIZE 1024
#define TX_BUFFER_SIZE 1024

#define MAXCHAR 1000				// max characters to read from txt file



char rx_buffer[RX_BUFFER_SIZE];		// buffer to store data from client
char tx_buffer[RX_BUFFER_SIZE];		// buffer to store data to be sent to client

char ipv4_addr_str[128];			// buffer to store IPv4 addresses as string
char ipv4_addr_str_client[128];		// buffer to store IPv4 addresses as string

int listen_sock;

char line_data[MAXCHAR];

FILE *input_fp, *dream_fp;

char dataToBeRead[1024]; 


int main() {
	
    char *input_file_name = "obstacle_pos.txt";
    char *dream = "dream.txt"; 

	char temp[1024] = {0};

	dream_fp = fopen(dream, "w");
	input_fp = fopen(input_file_name, "r");

	if (input_fp == NULL){
		printf("Could not open file %s\n",input_file_name);
		return 1;
	}

	int i = 0, k;
	int m_n = 0;
	
	while( fgets ( dataToBeRead, 1024, input_fp ) != NULL ) { 
        if(i % 2 == 0) {
        	printf("%d\n", dataToBeRead[0]);
        	while(m_n != (int)dataToBeRead[0] - 48) {
				fputs("@$@", dream_fp);
				fputs("\n", dream_fp);
				m_n++;
			}
        	if(1) {
	        	for(k = 0; dataToBeRead[k] != '\n'; k++) {
	        		if(dataToBeRead[k] == '(') {
	        			fputs("@", dream_fp);
	        			while(dataToBeRead[k] != ')') {
	        				char tem[1024];
	        				tem[0] = dataToBeRead[k];
	        				tem[1] = '\0';
	        			    fputs(tem, dream_fp) ;	
	        				k++;
						}
						fputs(")@", dream_fp);
						fputs("\n", dream_fp);
					}
				}
	        	fputs("@$@ coorecinates wala", dream_fp);
				fputs("\n", dream_fp);
			}
			m_n++;
		}
		
		i++;  
	}
	fclose(dream_fp) ; 
	fclose(input_fp);
	return 0;
}

