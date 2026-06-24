import unittest
import subprocess
import os
import glob

class TestCCompilation(unittest.TestCase):
    
    def test_gcc_syntax_integrity(self):
        # We test all C files in the directory to ensure they compile correctly
        # using the GCC -fsyntax-only flag, which checks for syntax/structural errors 
        # without generating .out binaries.
        base_dir = os.path.dirname(os.path.dirname(__file__))
        c_files = glob.glob(os.path.join(base_dir, "**/*.c"), recursive=True)
        
        self.assertTrue(len(c_files) > 0, "No C source files found to compile.")
        
        for file in c_files:
            # Execute GCC syntax check
            result = subprocess.run(
                ["gcc", "-fsyntax-only", file], 
                capture_output=True, 
                text=True
            )
            self.assertEqual(
                result.returncode, 
                0, 
                msg=f"GCC Compilation failed for {os.path.basename(file)}:\n{result.stderr}"
            )

if __name__ == '__main__':
    unittest.main()
