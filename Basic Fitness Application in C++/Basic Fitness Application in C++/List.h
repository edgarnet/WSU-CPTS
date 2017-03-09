#pragma once
#include "Header.h"
#include "FitnessAppWrapper.h"
typedef struct node
{
	FitnessAppWrapper FObj;
	struct node * pNext = nullptr;
}Node;
class List
{
public:
	List();
	~List();// fix this

	static Node * makeNode();
	static void insertInEnd(Node * pMem, Node ** headnode);
	
	friend std::ostream& operator<<(std::ostream& lhs, FitnessAppWrapper&rhs);

	void displayDailyDietPlan() const;
	void displayDailyExercisePlan() const;
	void displayWeeklyDietPlan()  const;
	void displayWeeklyExercisePlan() const;
	void storeDailyDietPlan(fstream& Dietfile) const;// list functions
	void storeDailyExercisePlan(fstream& Exercisefile) const;
	void storeWeeklyDietPlan(fstream& Dietfile) const ;
	void storeWeeklyExercisePlan(fstream& Exercisefile) const;
	void displayMenu(fstream& Dietfile,fstream& Exercisefile) const; 
	void editNode(fstream& Dietfile, fstream& Exercisefile) const;

	void AssembleList(fstream& Dietfile, fstream& Exercisefile, List &obj);
	Node * getHead() const;



private:
	Node *headnode;

};
