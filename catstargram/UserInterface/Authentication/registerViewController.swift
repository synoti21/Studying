//
//  registerViewController.swift
//  catstargram
//
//  Created by 안지완 on 2022/04/05.
//

import UIKit

class registerViewController: UIViewController {
    // MARK: - Properties
    var isValidEmail = false
    
    var isValidName = false
    
    var isValidNickname = false
    
    var isValidPassword = false
    
    @IBOutlet weak var signupButton: UIButton!
    //textfields
    
    @IBOutlet weak var emailTextField: UITextField!
    
    @IBOutlet weak var nameTextField: UITextField!
    
    @IBOutlet weak var nicknameTextField: UITextField!
    
    @IBOutlet weak var passwordTextField: UITextField!
    
    var textFields: [UITextField] {
        [emailTextField,nameTextField,nicknameTextField,passwordTextField]
    }
    
    
    // MARK: - Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()

    }
    
    // MARK: - Actions
    @objc
    func textFieldEditingChanged(_ sender: UITextField){
        
        let text = sender.text ?? ""
        switch sender{
        case emailTextField:
            self.isValidEmail = text.isValidEmail()
        case nameTextField:
            print("name")
        case nicknameTextField:
            print("nickname")
        case passwordTextField:
            print("password")
        default:
            fatalError("")
        }

    }
    
    
    
    // MARK: - Helpers
    private func setupTextField(){
        
        textFields.forEach{ tf in
            tf.addTarget(self, action: #selector(textFieldEditingChanged(_:)), for: .editingChanged)
        }
        
    
        
        
    }
    
    // 사용자가 입력한 회원정보 확인 -> UI 업데이트
    private func validateUserInfo(){
        
        if isValidEmail
            && isValidName
            && isValidNickname
            && isValidPassword{
            
            self.signupButton.backgroundColor = UIColor.facebookColor
        }else{
            self.signupButton.backgroundColor = .disabledButtonColor
        }
    }

}

extension String {
    func isValidEmail() -> Bool {
        // here, `try!` will always succeed because the pattern is valid
        let regex = try! NSRegularExpression(pattern: "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", options: .caseInsensitive)
        return regex.firstMatch(in: self, options: [], range: NSRange(location: 0, length: count)) != nil
    }
    
    func isValidPassword() -> Bool {
        let passwordRegex = "^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*()\\-_=+{}|?>.<,:;~`’]{8,}$"
        return NSPredicate(format: "SELF MATCHES %@", passwordRegex).evaluate(with: self)
    }
}
extension UIColor{
    static let facebookColor = UIColor(named: "facebookColor")
    
    static let disabledButtonColor = UIColor(named: "disabledButtonColor")
}
