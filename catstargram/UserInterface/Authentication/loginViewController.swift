 //
//  loginViewController.swift
//  catstargram
//
//  Created by 안지완 on 2022/04/05.
//

import UIKit
import Alamofire

class loginViewController: UIViewController {
    
    var email = String()
    var password = String()
   
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    

    @IBAction func emailTextFieldEditingChange(_ sender: UITextField) {
        
        let text = sender.text ?? ""
        self.email = text
        print(text)
    }

    @IBAction func passwordTextFieldEditingChange(_ sender: UITextField) {
        
        let text = sender.text ?? ""
        self.password = text
        print(text)
    }
    
    @IBAction func loginButtonDidTap(_ sender: UIButton) {
        //화면전환
        //1 스토리보드 생성
    }
    @IBAction func registerButtonDisTap(_ sender: UIButton) {
        let storyboard = UIStoryboard(name : "Main", bundle: nil)
        //viewController 생성
        let registerViewController = storyboard.instantiateViewController(withIdentifier: "RegisterVC") as! registerViewController
        //화면 전환 메소드 이용해서 화면 전환
//        self.present(registerViewController, animated: true, completion: nil)
        
        self.navigationController?.pushViewController(registerViewController, animated: true)
    
    }
}

