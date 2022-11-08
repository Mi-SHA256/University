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
    int DepositMoney(int depositedamount, int intialbalance);
    int withdrawMoney(int withdrawalamount, int intialbalance);
    void displayBalance(int intialbalance);
    int Transfer (int transfer, int intialbalance);
    void ChangeDetails();
    bool validateIP(char str []);
    bool EmailCheck(string email);
    bool NumberCheck(int num);
    // define any other function here.

    int id;
    char ipaddress[16];
    string email;

// Main Program
int main()
{
    int withdrawalamount, depositedamount, transfer, intialbalance = 10000, m = 1;

    cout << "\t **************** Banking Application ******************* \n";
    cout<< endl;

    cout << "**********Please provide your credentials :: " <<endl
    << " \t **** IP-Address" <<endl
    << "\t **** Email" << endl
    << "\t **** ID " << endl <<endl <<endl;

    cout << "\t ******** Enter Your IP Address :" ;
    cin.getline(ipaddress, 16);
    cout << endl;

    cout << "\t ******** Enter Your BCU Email Address:" ;
    cin >> email;
    cout << endl;

    cout << "\t ******** Enter Your ID :";
    cin >>id;
    cout << endl;

    cout << "******************** We are Checking Your Credentials ********************" << endl <<endl;

    Sleep(1000);


    bool checkresult= Validitycheck(ipaddress,email,id);
    while(m){

    if (checkresult) // if checkresult is true
    {
            cout <<endl<<endl;

            cout << " \t ***** Choose an option :: *****" << endl << endl;

            cout <<" \t   W : Withdraw" << endl
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
                        intialbalance = withdrawMoney(withdrawalamount, intialbalance);
                        t=false;
                }
                else if (input=="D" || input=="d"){
                    intialbalance = DepositMoney(depositedamount, intialbalance);
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
                    intialbalance = Transfer(transfer,intialbalance);
                     t=false;
                 }
                else if (input=="C" || input=="c"){
                     ChangeDetails();
                     t=false;
                }
                else if (input=="Q" || input=="q"){
                     cout << "QUIT";
                     m=false;
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
    else
    {
    cout<<"\t \t **** check result failed, Please try again ****";
    m=false;
    }

}
}
/* Function Definition */

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

    int DepositMoney(int depositedamount,int intialbalance)
    {

    // Get how much user want to deposit and display balance after adding
    cout << "Your Balance is " << intialbalance <<endl;
    cout << "Enter the amount you want to deposit" <<endl;
    cin >> depositedamount;
    intialbalance = intialbalance + depositedamount;
    cout << "Your Balance is " << intialbalance <<endl;
    return intialbalance;
    }

    int withdrawMoney(int withdrawalamount,int intialbalance)
    {
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
    return intialbalance;
    }


    // Function for Display Balance
    void displayBalance(int intialbalance)
    {
    // display balance after adding
    cout << "Your current balance is " << intialbalance <<endl;
    }



    //function for Transfer Money
    int Transfer(int transfer,int intialbalance)
    {

    cout << "Your current balance is " << intialbalance <<endl;
    cout << "Enter the amount you want to transfer" <<endl;
    cin >> transfer;
    if ( transfer >  intialbalance){


        cout << "Insufficient balance" <<endl;

    }
    else
    {
    intialbalance = intialbalance - transfer;
    cout << "Your current balance is " << intialbalance <<endl;

    }
    return intialbalance;
    }


    void ChangeDetails()
    {

    cout << "\t ******** Enter Your IP Address :" ;
    cin.ignore();
    cin.get();
    cin.getline(ipaddress, 16);
    cout << endl;

    cout << "\t ******** Enter Your Email Address:" ;
    cin >> email;
    cout << endl;

    cout << "\t ******** Enter Your ID :";
    cin >>id;
    cout << endl;

    }


bool validateIP(char str [])
        {

           int iparray [4];
           int i=0;


            char *token = strtok(str, ".");
            while (token != NULL)
            {
                int num = stoi(token);
                iparray[i]=num;
                token = strtok(NULL, ".");
                i++;
            }
            int getArrayLength = sizeof(iparray) / sizeof(int);

            if (getArrayLength-1 != 3)
            {
                return false;
            }


            for (int j=0; j<=getArrayLength-1; j++)
            {

                if (iparray[j] > 255 || iparray[j] < 0)
                {
                    return false;
                }
            }
             return true;
        }

    bool EmailCheck(string email)
    {
     const regex pattern("(\\w+)(\\.|_)?(\\w*)@bcu.ac.uk"); // your code for number check return true or false value. Lab 5A.
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
