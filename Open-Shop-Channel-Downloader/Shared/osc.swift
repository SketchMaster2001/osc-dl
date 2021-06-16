//
//  osc.swift
//  Open-Shop-Channel-Downloader
//
//  Created by Noah Pistilli on 2021-06-15.
//

import Foundation


struct OSCData: Codable, Identifiable {
    var display_name: String
    var coder: String
    var internal_name: String
    let id = UUID()
}

class OSCAPI {
    func getData(completion:@escaping ([OSCData]) -> ()) {
        guard let url = URL(string: "https://api.oscwii.org/v2/primary/packages") else { return }
        URLSession.shared.dataTask(with: url) { (data, _, _) in
            let users = try! JSONDecoder().decode([OSCData].self, from: data!)
            
            DispatchQueue.main.async {
                completion(users)
            }
        }
        .resume()
    }
}
