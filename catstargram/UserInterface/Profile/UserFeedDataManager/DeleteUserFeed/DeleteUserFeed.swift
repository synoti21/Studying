//
//  UserFeedDelete.swift
//  catstargram
//
//  Created by 안지완 on 2022/05/31.
//

import Foundation

struct DeleteUserFeed : Decodable {
    let isSuccess : Bool?
    let code :  Int?
    let message : String?
    let result : String?
}
