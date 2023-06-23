pipeline {
  agent any
  
  stages {
    stage('Test') {
      steps {
        echo 'Running tests...'
        // Execute your test commands here
        sh 'pytest test_sample.py'
      }
    }
  }
  
  post {
    always {
      echo 'Pipeline completed.'
    }
    success {
      echo 'Tests passed.'
    }
    failure {
      echo 'Tests failed.'
    }
  }
}
