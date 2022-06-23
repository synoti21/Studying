//
//  PostCollectionViewCell.swift
//  catstargram
//
//  Created by 안지완 on 2022/05/17.
//

import UIKit
import Kingfisher

class PostCollectionViewCell: UICollectionViewCell {
    
    
    
    @IBOutlet weak var postImageView: UIImageView!
    
    
    static let identifier = "PostCollectionViewCell"

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }
    
    public func setupData(_ imageURLStr: String?){
        //upload image of imageview
        guard let imageURLStr = imageURLStr else { return }
        
        if let url = URL(string: imageURLStr){
            postImageView.kf.setImage(
                with: url,
                placeholder: UIImage(systemName: "photo"))

        }
    }
    
}
