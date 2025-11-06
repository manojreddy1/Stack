//
//  AppDelegate.swift
//  Stack
//
//  Created by Manoj C on 18/06/25.
//

import Firebase
import FirebaseAnalytics

class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        FirebaseApp.configure()
        Analytics.setAnalyticsCollectionEnabled(true)
        Analytics.logEvent("screen_view1", parameters: [
            "test_timestamp": Date().timeIntervalSince1970
        ])
        if let firebaseApp = FirebaseApp.app() {
            print("Firebase Analytics configured for GA4 property: \(firebaseApp.options.projectID)")
        }
        return true
    }
}
