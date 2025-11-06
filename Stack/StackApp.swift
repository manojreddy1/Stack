//
//  StackApp.swift
//  Stack
//
//  Created by Manoj C on 19/07/24.
//

import SwiftUI

//@main
//struct StackApp: App {
//    var body: some Scene {
//        WindowGroup {
//            ContentView()
//        }
//    }
//}
@main
struct StackApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
