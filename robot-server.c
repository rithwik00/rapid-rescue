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

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <arpa/inet.h>


// Constants defined
#define SERVER_PORT 3333
#define RX_BUFFER_SIZE 1024
#define TX_BUFFER_SIZE 1024

#define MAXCHAR 1000				// max characters to read from txt file

// Global variables
struct sockaddr_in dest_addr;
struct sockaddr_in source_addr;

char rx_buffer[RX_BUFFER_SIZE];		// buffer to store data from client
char tx_buffer[RX_BUFFER_SIZE];		// buffer to store data to be sent to client

char ipv4_addr_str[128];			// buffer to store IPv4 addresses as string
char ipv4_addr_str_client[128];		// buffer to store IPv4 addresses as string

int listen_sock;

char line_data[MAXCHAR];

FILE *input_fp, *output_fp;

//by me
#define MAX_CLIENT 2
char send1[1024];
FILE *dream_fp;
int receive_from_send_to_client(int);

void createDream() {
		
	
	int i = 0, k;
	int m_n = 0;	
    char *dream = "dream.txt"; 
	char *input_file_name = "obstacle_pos.txt";
	char dataToBeRead[1024]; 
	dream_fp = fopen(dream, "w");
	input_fp = fopen(input_file_name, "r");

	if (input_fp == NULL){
		printf("Could not open file %s\n",input_file_name);
		return	;
	}

	
	while( fgets ( dataToBeRead, 1024, input_fp ) != NULL ) { 
        if(i % 2 == 0) {
        	//printf("%d\n", dataToBeRead[0]);
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
	        	fputs("@$@", dream_fp);
				fputs("\n", dream_fp);
			}
			m_n++;
		}
		
		i++;  
	}
	fclose(dream_fp) ; 
	fclose(input_fp);
}

//end by me

/*
* Function Name:	socket_create
* Inputs:			dest_addr [ structure type for destination address ]
* 					source_addr [ structure type for source address ]
* Outputs: 			my_sock [ socket value, if connection is properly created ]
* Purpose: 			the function creates the socket connection with the server
* Example call: 	int sock = socket_create(dest_addr, source_addr);
*/
int socket_create(struct sockaddr_in dest_addr, struct sockaddr_in source_addr){

	int addr_family;
	int ip_protocol;

	dest_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(SERVER_PORT);
	addr_family = AF_INET;
	ip_protocol = IPPROTO_IP;

	int my_sock;

	//edited code
	int len = sizeof(struct sockaddr_in); 
	int cli;
	my_sock = socket(PF_INET, SOCK_STREAM, 0);
	

	bind(my_sock,(struct sockaddr *) &dest_addr, len);

	
	listen(my_sock, MAX_CLIENT);
	printf("listening.....\n");

	while(1)
	{
		listen_sock = accept(my_sock,(struct sockaddr *) &source_addr, &len) ;	
		printf("\n NEW CLIENT CONNECTED IP : %s \n",inet_ntoa(source_addr.sin_addr));	
		//send(listen_sock ,hello, strlen(hello),0);
		receive_from_send_to_client(listen_sock);
		close(listen_sock);
	}
    //edit end      

	return my_sock;
}


/*
* Function Name:	receive_from_send_to_client
* Inputs:			sock [ socket value, if connection is properly created ]
* Outputs: 			None
* Purpose: 			the function receives the data from server and updates the 'rx_buffer'
*					variable with it, sends the obstacle position based on obstacle_pos.txt
*					file and sends this information to the client in the provided format.
* Example call: 	receive_from_send_to_client(sock);
*/
int receive_from_send_to_client(int sock){


	//edit code
	char *hello = "Hello from server";
	//createDream();
	char *dream = "dream.txt"; 
	char dataToBeRead[1024];
	dream_fp = fopen(dream, "r");
	int valread;

	
	while( fgets ( dataToBeRead, 1024, dream_fp ) != NULL ) {
		valread = read(sock, rx_buffer, 1024);
		printf("recieved ===>%s %d\n", rx_buffer, valread);
		printf("sent ===>%s\n", dataToBeRead);
		send(sock , dataToBeRead, strlen(dataToBeRead),0);

	}

	/*read = getline(&line, &len, input_fp);
	int t = 4;
    while ( t--) {
        printf("Retrieved line of length %zu:\n", read);
	//	send(listen_sock ,line, strlen(hello),0);
        printf("i am sending this===>%s", line);
		send(listen_sock ,line, strlen(line),0);
		read = getline(&line, &len, input_fp);
    }*/

	//editend
	fclose(dream_fp);
	return 0;
}


int main() {
	
    char *input_file_name = "obstacle_pos.txt";
	char *output_file_name = "data_from_client.txt";

	// Create socket and accept connection from client
	int sock = socket_create(dest_addr, source_addr);

	input_fp = fopen(input_file_name, "r");

	if (input_fp == NULL){
		printf("Could not open file %s\n",input_file_name);
		return 1;
	}

	fgets(line_data, MAXCHAR, input_fp);

	output_fp = fopen(output_file_name, "w");

	if (output_fp == NULL){
		printf("Could not open file %s\n",output_file_name);
		return 1;
	}

	while (1) {

		// Receive and send data from client and get the new shortest path
		receive_from_send_to_client(sock);

		// NOTE: YOU ARE NOT ALLOWED TO MAKE ANY CHANGE HERE
		fputs(rx_buffer, output_fp);
		fputs("\n", output_fp);

	}

	return 0;
}

