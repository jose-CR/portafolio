<x-app-layout>
    <div class="p-16 mt-8 text-gray-900 dark:text-gray-100">

        <div class="p-4 text-gray-900 dark:text-gray-100">
            <section class="flex items-center justify-center">
                <button class="bg-green-500 text-white font-semibold py-2 px-6 rounded-lg shadow-lg transition-all duration-300 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-red-400">
                    <a href="{{ route('projects.create') }}" class="w-full h-full inline-block text-center">
                        create +
                    </a>
                </button>
            </section>  
        </div>

        <livewire:project.project-table />
    </div>
</x-app-layout>
