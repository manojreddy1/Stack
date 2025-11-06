//
//  ContentView.swift
//  Stack
//
//  Created by Manoj C on 19/07/24.
//

import SwiftUI

struct ContentView: View {
    @State var isActive : Bool = false

    var body: some View {
        NavigationView {
            NavigationLink(
                destination: ContentView2(rootIsActive: self.$isActive),
                isActive: self.$isActive
            ) {
                Text("Hello, World!")
            }
            .isDetailLink(true)
            .navigationBarTitle("Root")
        }
    }
}

struct ContentView2: View {
    @Binding var rootIsActive : Bool

    var body: some View {
        NavigationLink(destination: ContentView3(shouldPopToRootView: self.$rootIsActive)) {
            Text("Hello, World #2!")
        }
        .isDetailLink(false)
        .navigationBarTitle("Two")
    }
}

struct ContentView3: View {
    @Binding var shouldPopToRootView : Bool

    var body: some View {
        VStack {
            Text("Hello, World #3!")
            Button (action: { self.shouldPopToRootView = false } ){
                Text("Pop to root")
            }
        }.navigationBarTitle("Three")
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

#Preview {
    ContentView()
}
//import SwiftUI
//
//struct ContentView: View {
//    var body: some View {
//        NavigationStack {
//            HomeView()
//        }
//    }
//}
//
//struct HomeView: View {
//    var body: some View {
//        NavigationLink("Go to Detail View", destination: DetailView())
//            .navigationTitle("Home")
//    }
//}
//
//struct DetailView: View {
//    @EnvironmentObject var navigationState: NavigationState
//
//    var body: some View {
//        VStack {
//            Text("Detail View")
//            Button("Go deeper") {
//                navigationState.path.append("Another View")
//            }
//        }
//        .navigationTitle("Detail")
//        .toolbar {
//            ToolbarItem(placement: .navigationBarLeading) {
//                Button(action: {
//                    navigationState.path.removeLast(navigationState.path.count)
//                }) {
//                    Image(systemName: "chevron.left")
//                        .foregroundColor(.blue)
//                }
//            }
//        }
//    }
//}
//
//class NavigationState: ObservableObject {
//    @Published var path = NavigationPath()
//}



