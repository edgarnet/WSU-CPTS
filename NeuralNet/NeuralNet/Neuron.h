#pragma once
#include "Header.h"
#include "Synapse.h"
#include <vector>

class Neuron
{
public:
	
	Neuron(int numOutputs, int MyIndex);
	typedef std::vector<Neuron> Layer;
	void setOutput(double val);
	double getOutput()const;
	void feedForward(Layer &prevLayer);
	void calcOutputGradients(double targetOutputs);
	void calcHiddenGradients(const Layer &nextLayer);
	void updateInputWeights(Layer &prevLayer);
private:
	double mOutput;
	vector<Synapse> mOuputWeights;
	static double randomWeight();
	double sumDOW(const Layer &nextLayer);
	int mMyIndex;
	static double transferFunction(double sum);
	static double transferFunctionDerivative(double sum);
	double mGradient;
	double Neuron::overallNetLearningRate;//0.0 through 1.0
	double Neuron::momentum;//0.0 through 1.0,multiplyer of last weight change
};
