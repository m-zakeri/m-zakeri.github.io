Title: Compilers
Date: 2021-03-23 00:23
Tags: courses, teaching
Author: Morteza
Summary: Compiler design and constructions, Undergraduate course (Bachelor). The course is designed to:
- Provide an in-depth understanding of the principles, techniques, and tools used in the design and implementation of compilers.
- Equip students with the ability to write and optimize programs by understanding how high-level code is translated into machine-level instructions.
- Introduce concepts of language parsing, code generation, and optimization techniques that are critical for the development of efficient and reliable software.
- Foster the ability to analyze and improve existing compiler systems, as well as design new ones from scratch.


## Objectives
By the end of this course, students will be able to:
1. Understand the fundamental phases of a compiler, including lexical analysis, syntax analysis, semantic analysis, code generation, and optimization.
2. Develop skills to implement key components of a compiler, such as parsers, symbol tables, and intermediate code generators.
3. Recognize and utilize various parsing techniques, including top-down and bottom-up parsing strategies.
4. Apply optimization techniques to improve the performance of compiled code.
5. Gain exposure to modern tools and technologies used in compiler construction, such as Lex and Yacc.


## Syllabus
### 1. Introduction to Compiler Design
- Role of a compiler in the software development lifecycle
- Overview of programming languages and their features
- Architecture of a compiler

### 2. Lexical Analysis
- Lexical tokens, patterns, and lexemes
- Design of lexical analyzers
- Introduction to Lex and its usage

### 3. Syntax Analysis
- Context-free grammars and parse trees
- Top-down parsing (recursive descent, LL) and bottom-up parsing (LR, LALR)
- Error detection and recovery mechanisms in parsers

### 4. Semantic Analysis
- Role of semantic analysis in a compiler
- Type checking and type inference
- Symbol tables and attribute grammars

### 5. Intermediate Code Generation
- Representations such as three-address code, quadruples, and abstract syntax trees
- Translating high-level constructs into intermediate representations

### 6. Code Optimization
- Local vs global optimization techniques
- Loop optimizations, dead code elimination, and inlining
- Role of data-flow analysis in optimization

### 7. Code Generation
- Instruction selection and register allocation
- Basic blocks and flow graphs
- Generating efficient machine-level code

### 8. Advanced Topics
- Just-In-Time (JIT) Compilation
- Compiler frameworks (LLVM, GCC)
- Introduction to domain-specific languages (DSLs)

### 9. Project and Case Studies
- Design and implementation of a small-scale compiler
- Case studies on modern compiler systems and frameworks

---


## Teaching assistant

### Foreword
I was teaching assistant of Compiler Design and Construction B.Sc. course by [Dr. Saeed Parsa](http://parsa.iust.ac.ir/){:target="_blank"} for seven semesters (more than three years) at Iran University of Science and Technology. Our teaching materials during these three years are available to view and download.

I put all source code that I developed to practically teach compiler  to students on the GitHub page, the [IUST compiler course](http://parsa.iust.ac.ir/courses/compilers/){:target="_blank"}. 


### Useful links

* [ISUT Compiler Course Official page](http://parsa.iust.ac.ir/courses/compilers/){:target="_blank"}
  
* [ISUT Compiler Course GitHub Page (in English)](https://m-zakeri.github.io/IUSTCompiler/){:target="_blank"}

* [ISUT Compiler Course GitHub Page (in Persian)](https://compileriust.github.io/){:target="_blank"}


### Projects

I designed and planned some **practical** projects about the applications of compiler science in **program analysis**.
The projects shown in Table 1 have been assigned to the students who take the IUST compiler course during different semesters. Click on the link in the "Project" column to see the project proposal. 


**Table 1:** Compiler projects.

 | Project               	                                                                                                      |     Description                                                                                         	|     Semesters                    	|     Courses                             	|
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------	|----------------------------------	|-----------------------------------------	|
| [OpenUnderstand  2](https://m-zakeri.github.io/IUSTCompiler/projects/core_symbol_table_development/)    	                    |     Low-level source   code metrics calculation                                                         	|     Spring 2022                  	|     Compiler                            	|
| [OpenUnderstand](https://m-zakeri.github.io/IUSTCompiler/projects/core_symbol_table_development/)        	                   |     Symbols table   development                                                                         	|     Fall 2021,   Spring 2022,    	|     Compiler                            	|
| [QualityMeter](https://m-zakeri.github.io/IUSTCompiler/projects/core_software_metrics_development/)          	               |     - Source code   quality attribute computation     - Refactoring   opportunity detection             	|     Fall 2021                    	|     Advanced compiler                   	|
| [CodART 2](https://m-zakeri.github.io/IUSTCompiler/projects/core_code_smell_development/)              	                     |     Source code   smell detection                                                                       	|     Spring 2021   (Cancelled)    	|     Compiler                            	|
| [CodART](https://m-zakeri.github.io/IUSTCompiler/projects/core_refactoring_to_design_patterns_development/)                	 |     Source code   refactoring                                                                           	|     Fall 2020,   Spring 2021,    	|     Compiler                            	|
| [CodART](https://m-zakeri.github.io/IUSTCompiler/projects/core_refactorings_development/)                	                   |     Refactoring   to design pattern at the source code level                                            	|     Fall 2020                    	|     Advanced compiler                   	|
| [CleanCode](https://m-zakeri.github.io/IUSTCompiler/projects/core_clean_code_development/)            	                      |     Source code   smell detection                                                                       	|     Fall 2019,   Spring 2020     	|     Compiler                            	|
| [CodA](https://m-zakeri.github.io/IUSTCompiler/projects/core_source_code_instrumentation_development/)                  	    |     Source code instrumentation   and testbed analysis tool                                             	|     Fall 2018                    	|     Compiler /     Advanced compiler    	|
| [ANTLR MiniJava](https://m-zakeri.github.io/Compilers/projects/mini_java_compiler_development/)        	                     |     Parse-tree   and intermediate code generation for the MiniJava programming language with   ANTLR    	|     Fall 2016,   Spring 2017     	|     Compiler                            	|
| 	                                                                                                                            |                                                                                                         	|                                  	|                                         	|





## As a student

I always enjoy learning about compilers, code transformation, and their application in automated software engineering. I firmly believe that the next generation of software engineers are intelligent white-box compilers! Such compilers are structure-aware, context-aware, and domain-aware, assisting the programmer in writing high-quality and testable programs. 
Compilers helped artificial intelligence (AI) in the past, and now AI boosts compilers!


