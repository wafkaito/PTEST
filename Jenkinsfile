pipeline {
    agent any

    environment {
        allureReportPath = 'reports'
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    allureReportPaths = []  // List to store Allure report paths
                    sh 'pip install -r requirements.txt'
                }
            }
        }  
        stage('Run Tests 1 ') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    // Run pytest command and generate test result data
                    sh 'pytest test_ex.py --alluredir=Reports'
                    
                    // Append Allure report path to the list
                    script {
                        allureReportPaths.add("${allureReportPath}/")
                    }
                }
            }
        }
        stage('Run Tests 2 ') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    // Run pytest command and generate test result data
                    sh 'pytest test_ex1.py --alluredir=Reports'
                    
                    // Append Allure report path to the list
                    script {
                        allureReportPaths.add("${allureReportPath}/")
                    }
                }
            }
        }
        stage('Run Tests 3 ') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    // Run pytest command and generate test result data
                    sh 'pytest test_ex1.py --alluredir=Reports'
                    
                    // Append Allure report path to the list
                    script {
                        allureReportPaths.add("${allureReportPath}/")
                    }
                }
            }
        }
    }

    post {
        always {
            // Publish accumulated Allure reports
            allure([
                includeProperties: false,
                jdk: '',
                results: allureReportPaths.collect { path -> [path: path] }
            ])
        }
    }
}
