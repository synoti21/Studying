//
//  StoryCollectionViewCell.swift
//  catstargram
//
//  Created by 안지완 on 2022/05/10.
//

import UIKit

class StoryCollectionViewCell: UICollectionViewCell {

    @IBOutlet weak var viewImageViewBackground: UIView!
    @IBOutlet weak var ImageViewUserProfile: UIImageView!
    @IBOutlet weak var viewUserProfileBackground: UIView!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
        viewImageViewBackground.layer.cornerRadius = 24
        viewUserProfileBackground.layer.cornerRadius = 23.5
        ImageViewUserProfile.layer.cornerRadius = 22.5
        ImageViewUserProfile.clipsToBounds = true
    }

}
