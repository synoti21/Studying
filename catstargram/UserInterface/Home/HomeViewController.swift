//
//  HomeViewController.swift
//  catstargram
//
//  Created by 안지완 on 2022/04/28.
//

import UIKit
import Kingfisher

class HomeViewController: UIViewController{
    
    var arrayCat : [FeedModel] = []
    
    let imagePickerViewController = UIImagePickerController()

// MARK: - 초기설정, delegate및 datasource 등록 및 테이블 뷰 구성요소 연동
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.delegate = self
        tableView.dataSource = self
        tableView.separatorStyle = .none
        let feedNib = UINib(nibName: "FeedTableViewCell", bundle: nil)
        tableView.register(feedNib, forCellReuseIdentifier: "FeedTableViewCell")
        let storyNib = UINib(nibName: "StoryTableViewCell", bundle: nil)
        tableView.register(storyNib, forCellReuseIdentifier: "StoryTableViewCell")
        // Do any additional setup after loading the view.
        
        let input = FeedAPIInput(limit: 30, page: 10)
        FeedDataManager().feedDataManager(input, self)
        
        imagePickerViewController.delegate = self
    }
    @IBAction func buttonGoAlbum(_ sender: Any) {
        self.imagePickerViewController.sourceType = .photoLibrary
        self.present(imagePickerViewController, animated: true, completion: nil)
    }
    

    @IBOutlet weak var tableView: UITableView!
    

}

// MARK: - tableView에 대한 Delegate 및 DataSource 설정
extension HomeViewController : UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return arrayCat.count + 1
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        if indexPath.row == 0{ //indexpath의 첫번째 행은 storyTableViewCell을 배치한다.
            guard let cell = tableView.dequeueReusableCell(withIdentifier: "StoryTableViewCell",for : indexPath) as? StoryTableViewCell
            else{
                return UITableViewCell()
            }
            return cell
        }else{ //그외의 다른 행, storyTableView 아래의 행에는 FeedTableViewCell로 가득 채운다.

        guard let cell = tableView.dequeueReusableCell(withIdentifier:  "FeedTableViewCell",for:indexPath) as? FeedTableViewCell else {
            return UITableViewCell()
        }
            if let urlString = arrayCat[indexPath.row - 1].url { //현재 indexPath의 행은 '1'부터 FeedTable이 시작되므로, arrayCat 구조체의 FeedModel을 순서에 맞춰 이미지를 채운다. dequeueResuableCell을 보면 알겠지만, 실시간으로 채워진다.
                let url = URL(string: urlString)
                cell.ImageViewFeed.kf.setImage(with: url); //IBOutlet의 imageViewFeed의 이미지를 url을 본따서 얻은 이미지로 채운다.
            }
        return cell
        }
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        if indexPath.row == 0{
            return 80
        }else{
            return 600
        }
    }
    
    func tableView(_ tableView: UITableView, willDisplay cell: UITableViewCell, forRowAt indexPath: IndexPath) {
        guard let tableViewCell = cell as? StoryTableViewCell else{
            return
        }
        
        tableViewCell.setCollectionViewDataSourceDelegate(dataSourceDelegate: self, forRow: indexPath.row)
    }
}

// MARK: - CollectionView에 대한 Deleagate 및 DataSource 설정 (Catstargram의 Story)
extension HomeViewController : UICollectionViewDelegate, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout{
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return 10 //스토리가 노출될 최대 갯수 = 10개
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "StoryCollectionViewCell", for: indexPath) as? StoryCollectionViewCell else{
            return UICollectionViewCell()
        }
        return cell //스토리 CollectionViewCell을 재사용
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: 50, height: 60)
    }
}

// MARK: - 피드에 노출될 게시물의 사진과 서버 연동
extension HomeViewController {
    func successAPI(_ result : [FeedModel]){
        arrayCat = result
        tableView.reloadData() //사진을 불러오는데에 성공하면 이를 FeedModel 배열에 넣은 후 새로고침
    }
}

// MARK: - 이미지 업로드
extension HomeViewController : UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) { //앨범에서 선택한 이미지의 InfoKey를 가져옴
        if let image = info[UIImagePickerController.InfoKey.originalImage] as? UIImage{
            let imageString = "gs://catstargram-d7fbf.appspot.com/Cat" //가져온 이미지의 image가 존재하면 해당 url에 업로드
            let input = FeeduploadInput(content: "저희 상이입니다.", postImgsUrl: [imageString])
            FeedUploadDataManager().posts(self, input)
            
            self.dismiss(animated: true, completion: nil)
        }
    }
}
