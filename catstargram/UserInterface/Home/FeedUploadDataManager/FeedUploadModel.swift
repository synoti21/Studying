//
//  FeedUploadModel.swift
//  catstargram
//
//  Created by 안지완 on 2022/05/22.
//

struct FeedUploadModel : Decodable {
    var isSuccess : Bool
    var code : Int
    var message : String
    var result : FeedUploadResult
}

struct FeedUploadResult : Decodable {
    var postIdx : Int?
}
