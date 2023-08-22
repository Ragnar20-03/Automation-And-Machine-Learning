#include<iostream>
using namespace std ; 

template <class T>
struct DCL {
    struct DCL * next ;
    struct DCL * prev ;
    T data;

    DCL(T data)
    {
        this.data = data;
        this.next = nullptr;
        this.prev = nullptr;
    }
    
};

template <class T >
class LinkedList {

    private :
    DCL <T> * Head ; 
    DCL <T> * Tail ; 
    int iCount ;

    LinkedList () ;
    void InsertFirst ( T) ;
    void InsertLast ( T) ;
    void InsertAtPos ( T , pos) ;
    void DeleteFirst ( ) ;
    void DeleteLast ( ) ;
    void DeleteAtPos ( No) ;
    
};

template <class T>
LinkedList <T> :: LinkedList()
{
    this.Head = nullptr;
    this.Tail = nullptr;
    this.iCount = 0 ; 
} 

template <class T>
void LinkedList <T> :: InsertFirst(T data){
    struct DCL <T> * newn = new DCL (data);
    if (Head == nullptr)
    {
        Head = newn;
        Tail = newn;
    }
    else 
    {
        newn -> next = *Head;
        *Head -> prev = newn;
        *Head = newn;
    }
    Tail = 

}

int main()
{


    return 0;
}