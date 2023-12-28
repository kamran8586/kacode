from rest_framework import viewsets
from .models import Problem , Submission
from .serializers import ProblemSerializer , SubmissionSerializer
from subprocess import run, PIPE
import os
class ProblemView(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class SubmissionView(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    def get_queryset(self):
        problem_id = self.kwargs['problem_id']
        problem_instance = Problem.objects.get(pk = problem_id)
        user = self.request.user
        return Submission.objects.filter(problem = problem_instance , user = user)

    def perform_create(self, serializer):
        problem_id = self.kwargs['problem_id']
        user = self.request.user
        problem_instance = Problem.objects.get(pk = problem_id)
        serializer.save(user = user , problem = problem_instance)
        input_data = self.request.data.get('input_data')

        # Run code execution logic with optional input
        self.execute_code(serializer, input_data)

        # Call the parent class's perform_create to execute default behavior
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        problem_id = self.kwargs['problem_id']
        user = self.request.user
        problem = Problem.objects.get(pk = problem_id)

        serializer.save(user = user , problem = problem)
        input_data = self.request.data.get('input_data')

        # Run code execution logic with optional input
        self.execute_code(serializer, input_data)

        # Call the parent class's perform_update to execute default behavior
        return super().perform_update(serializer)
    
    def execute_code(self, serializer, input_data=None):
    # Retrieve the C++ code from the serializer
        cpp_code = serializer.validated_data.get('code', '')

        # Save the user's C++ code to a temporary file
        cpp_code_filename = 'temp_submission.cpp'
        with open(cpp_code_filename, 'w') as cpp_file:
            cpp_file.write(cpp_code)

        # Run the code compilation and execution
        compile_command = f'g++ -o temp_submission -x c++ {cpp_code_filename}'
        run_command = './temp_submission.exe'

        # Use subprocess to run the commands
        compile_process = run(compile_command, text=True, stdout=PIPE, stderr=PIPE)

        if compile_process.returncode == 0:
            # If compilation is successful, run the executable with optional input
            run_process = run(run_command, input=input_data, stdout=PIPE, stderr=PIPE)

            # Update the result field in the serializer
            result = run_process.stdout.decode() + run_process.stderr.decode()
            serializer.validated_data['output'] = result
        else:
            # If compilation fails, update the result field with the compilation error
            result = compile_process.stderr
            serializer.validated_data['output'] = result
        
        # Delete the temporary C++ file
        os.remove(cpp_code_filename)
