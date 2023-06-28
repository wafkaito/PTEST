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
                }
            }
        }

        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/wafkaito/PTEST.git'
            }
        }
        
        stage('Run Tests 1 ') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    // Run pytest command and generate test result data
                    bat 'pytest test_sample.py --alluredir=Reports'
                    
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
                    bat 'pytest test_sampl.py --alluredir=Reports'
                    
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
                    bat 'pytest test_sample.py --alluredir=Reports'
                    
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