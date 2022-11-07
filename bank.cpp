// CPP Program to demonstrate main() with
// return type
#include <iostream>
#include <string>
#include<windows.h>
#include <regex>
#include<stdio.h>

#include <string.h>

#include <vector>

#include <iterator>
#include <list>

#include <stdarg.h>

using namespace std;

    /* FUNCTION DEFINITION */

    bool Validitycheck(char ip[16], string email, int num);
    void DepositMoney(int depositedamount, int intialbalance);
    void withdrawMoney(int withdrawalamount, int intialbalance);
    void displayBalance(int intialbalance);
    void Transfer (int transfer, int intialbalance);
    void ChangeDetails();
    bool validateIP(char str []);
    bool EmailCheck(string email);
    bool NumberCheck(int num);
    // define any other function here.




// Main Program
int main()
{
    int withdrawalamount, depositedamount, transfer, id, intialbalance;
    intialbalance=10000;
    char ipaddress[16];
    string email;

    cout << "\t **************** WELCOME MR C++ EXPERT TO MY BANKING APPLICATION ******************* \n";
    cout<< endl;

    cout << "**********Please provide your credentials that are :: " <<endl
    << " \t **** IP-Address" <<endl
    << "\t **** Email" << endl
    << "\t **** ID " << endl <<endl <<endl;

    cout << "\t ******** Enter Your IP Address :" ;
    cin.getline(ipaddress, 16);
    cout << endl;

    cout << "\t ******** Enter Your Email Address:" ;
    cin >> email;
    cout << endl;

    cout << "\t ******** Enter Your ID :";
    cin >>id;
    cout << endl;

    cout << "******************** WAIT !! We are Checking Your Credentials ********************" << endl <<endl;

    Sleep(1000);

    /* CHECKING VALIDITY OF CREDENTIALS */
    bool checkresult= Validitycheck(ipaddress,email,id); // This line call a function validitycheck with arguments ipaddress, email and id. The return
                                                         // value is true or false

   // If ValidtyCheck is true move to next lines of code otherwise terminate processing
    if (checkresult) // if checkresult is true
    {
            cout <<endl<<endl;

            cout << " \t ***** What you want to Do ??? Choose the Action character *****" << endl << endl;

            cout <<" \t   W : Money Withdraw" << endl
            <<"\t   D : Deposit" << endl
            <<"\t   B : Balance" << endl
            <<"\t   T : Transfer" << endl
            <<"\t   C : Change Details" << endl
            <<"\t   Q : Quit or Exit" << endl << endl ;

            string input;
            cin >> input;
            bool t=true;

            while (t)
            {
                if (input=="W" || input=="w"){
                        cout<<"Calling Withdraw Option -";
                        withdrawMoney(withdrawalamount, intialbalance);
                        t=false;
                }
                else if (input=="D" || input=="d"){
                    cout << "Deposit";
                    DepositMoney(depositedamount, intialbalance);
                    t=false;
                }
                else if (input=="B" || input=="b"){
                     cout << "Display Balance";
                     displayBalance(intialbalance);
                     t=false;
                }
                else if (input=="T" || input=="t")
                 {
                    cout << "Transfer Balance";
                    Transfer(transfer,intialbalance);
                     t=false;
                 }
                else if (input=="C" || input=="c"){
                     cout << "Change Deails";
                     ChangeDetails();
                     t=false;
                }
                else if (input=="Q" || input=="q"){
                     cout << "QUIT";
                     t=false;
                }
                 else
                 {
                  cout << endl;
                  cout<< "Select correct value for Example W for Withdraw .... Try Again" <<endl<<endl;
                  cout <<"   W : Money Withdraw" << endl
                    <<"   D : Deposit" << endl
                    <<"   B : Balance" << endl
                    <<"   T : Transfer" << endl
                    <<"   T : Transfer" << endl
                    <<"   C : Change Details" << endl
                    <<"   Q : Quit or Exit" << endl << endl ;
                  cin >> input;
                 }
                }
    }
    else // if checkresult is false
    {
    cout<<"\t \t **** check result failed, Please try again ****";
    }

}

/* Function Definition */

    // Function for Validity Check

    bool  Validitycheck(char ip[16], string email, int num)
    {
    bool check;
    bool IPValidty = validateIP(ip);
    bool EmailValidity = EmailCheck(email);
    bool NumValidity = NumberCheck(num);


    if (IPValidty == true && EmailValidity == true && NumValidity == true)
    {
      cout << " \t \t Check Successful -------------- " <<endl;
      return true;
    }
    else
    {
    cout <<"\t \t Check Failed -------------- " <<endl;
      return false;
    }

   }

//
//
//
//
// I don't know what your criteria are, and I want you to learn how to do this yourself, but here's a start.
// I'm not sure what you mean by "IPCheck" and "EmailCheck" and "NumberCheck" but I'm assuming they are functions that return a bool.
// I'm also assuming that you want to check that the IP address is valid, the email address is valid, and the number is valid.
//
//
//
//





     // Function for Deposit
    void DepositMoney(int depositedamount,int intialbalance)
    {

    // Get how much user want to deposit and display balance after adding
    cout << "Your Balance is " << intialbalance <<endl;
    cout << "Enter the amount you want to deposit" <<endl;
    cin >> depositedamount;
    intialbalance = intialbalance + depositedamount;
    cout << "Your Balance is " << intialbalance <<endl;
    return;
    }







    // Function for Withdraw

    void withdrawMoney(int withdrawalamount,int intialbalance)
    {



// Get how much user want to withdraw and display balance after minus
        cout << "Your current balance is " << intialbalance <<endl;
        cout << "Enter the amount you want to withdraw: " <<endl;
        cin >> withdrawalamount;

    if (withdrawalamount > intialbalance){


        cout << "Insufficient funds" <<endl;
    }
    else {

        intialbalance = intialbalance -  withdrawalamount;
        cout << "Your current balance is " << intialbalance <<endl;
    }
    return;
    }






    // Function for Display Balance
    void displayBalance(int intialbalance)
    {
    // display balance after adding
    cout << "Your current balance is " << intialbalance <<endl;
    return;
    }



    //function for Transfer Money
    void Transfer(int transfer,int intialbalance)
    {
        // Get how much user want to transfer and display balance after transfer
    cout << "Your current balance is " << intialbalance <<endl;
    cout << "Enter the amount you want to transfer" <<endl;
    cin >> transfer;
    if ( transfer >  intialbalance){


        cout << "Insufficient balance" <<endl;
        return;
    }
    else
    {
    intialbalance = intialbalance - transfer;
    cout << "Your current balance is " << intialbalance <<endl;
    return;
    }
    }
     // Function for change Details






    void ChangeDetails()
    {

    }







bool validateIP(char str [])
        {

           int iparray [4]; // this will hold values when "." is removed from the string e.g 192.168.1.1 ====> 192 168 1 1
           int i=0;

            // The code to split the string using "." operator
            char *token = strtok(str, ".");
            while (token != NULL)
            {
                int num = stoi(token);   // this line convert string to integer. Example handling ip address 192.168.1.1
                iparray[i]=num;          // this line puts num to iparray for example iparray[0]=192, iparray[1]=168, iparray[2]=1, iparray[3]=1,
                token = strtok(NULL, ".");
                i++;
            }
            int getArrayLength = sizeof(iparray) / sizeof(int); //sizeof(iparray) is library function returns size in bytes when need to find number of elements
                                                              // in iparray thats why we divided it by sizeof(int) which is 4 bytes.
        // if the token size is not equal to four
            if (getArrayLength-1 != 3)
            {
                return false;
            }

            // validate each field of the IP-address
            for (int j=0; j<=getArrayLength-1; j++)
            {
                // check number if greater >0 and less than 255
                if (iparray[j] > 255 || iparray[j] < 0)
                {
                    return false;
                }
            }
             return true;
        }

    bool EmailCheck(string email)
    {
     const regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+"); // your code for number check return true or false value. Lab 5A.
     if (regex_match(email,pattern))
     {
         return true;
     }
      else
     {
      return false;
     }
    }



    bool NumberCheck(int num)
    {
        // code for number check, return true or false. Hint simple if statement for > and < logic
    // simple loop on how it should be done based on the number digit, you can use while loop or for loop but dont use a number use a variable that you can increment
    for (int i=0; i<4; i++)
    {
        if (num > 0000 && num < 9999)
        {
          return true;
        }
        else
        {
          return false;
        }
    }
    }
    // return true;
    // }
    // Any other Function. Do not forget to declare it as well
