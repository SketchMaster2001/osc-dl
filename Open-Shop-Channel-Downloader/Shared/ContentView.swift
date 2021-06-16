//
//  ContentView.swift
//
//  Created by Noah Pistilli on 2021-06-15.
//

import SwiftUI

struct OSC_DB: View {
    @State var data: [OSCData] = []
    
    var body: some View {
        List(data) {data in
            HStack {
                Text(data.display_name)
                    .font(.headline)
                
                Text(data.coder)
                    .font(.subheadline)
            }
        }
        .onAppear() {
                
                OSCAPI().getData { (data) in
                    self.data = data
                }
            }
        }
    }

